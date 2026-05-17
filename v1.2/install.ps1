<#
.SYNOPSIS
  Install the fullstack-skills pack into a project as a Claude Code plugin
  (NOT under .claude/skills/), and update the project's .gitignore for you.

.DESCRIPTION
  Copies the whole pack (RULES.md, AGENTS.md, skills/, .claude-plugin/) into
  <Project>\<Dir> as one self-contained plugin directory. The pack tree is kept
  intact so each skill's `../../RULES.md` reference still resolves.

  After install, load it per session with:
      claude --plugin-dir "<Project>\<Dir>"

.PARAMETER Project
  Absolute path to the target project root. Required.

.PARAMETER Dir
  Sub-directory name created inside the project for the pack.
  Default: ".skillpack" (kept out of .claude/ as requested).

.EXAMPLE
  pwsh C:\Users\kil\Desktop\ai_skills\v1.1\install.ps1 -Project "C:\code\my-app"
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)] [string] $Project,
  [string] $Dir = ".skillpack"
)

$ErrorActionPreference = "Stop"
$src = $PSScriptRoot
if (-not (Test-Path (Join-Path $src "RULES.md"))) {
  throw "Run this script from inside the pack (RULES.md not found next to install.ps1)."
}
if (-not (Test-Path $Project)) { throw "Project path not found: $Project" }

$dest = Join-Path $Project $Dir
New-Item -ItemType Directory -Force $dest | Out-Null

# Copy the pack tree intact (RULES.md/AGENTS.md must stay 2 levels above each SKILL.md)
foreach ($item in @("RULES.md", "AGENTS.md", "skills", ".claude-plugin")) {
  $from = Join-Path $src $item
  if (Test-Path $from) {
    Copy-Item $from (Join-Path $dest $item) -Recurse -Force
  }
}

# Verify
$skillCount = (Get-ChildItem (Join-Path $dest "skills") -Directory).Count
$rulesOk    = Test-Path (Join-Path $dest "RULES.md")
$agentsOk   = Test-Path (Join-Path $dest "AGENTS.md")
Write-Host "Installed to: $dest"
Write-Host ("  skills: {0}  RULES.md: {1}  AGENTS.md: {2}" -f $skillCount, $rulesOk, $agentsOk)

# Idempotently add the pack dir to the project's .gitignore
$giPath = Join-Path $Project ".gitignore"
$line   = "/$Dir/"
$marker = "# fullstack-skills pack (local plugin, not tracked)"
$gi     = if (Test-Path $giPath) { Get-Content $giPath -Raw } else { "" }
if ($gi -notmatch [regex]::Escape($line)) {
  $block = "`n$marker`n$line`n"
  Add-Content -Path $giPath -Value $block -Encoding utf8
  Write-Host "Added '$line' to $giPath"
} else {
  Write-Host "'$line' already in .gitignore — skipped"
}

Write-Host ""
Write-Host "NEXT STEPS:"
Write-Host "  1. Load the plugin for a session:"
Write-Host "       claude --plugin-dir `"$dest`""
Write-Host "     (skills invoked as /fullstack-skills:<name>, e.g. /fullstack-skills:bug-debugging)"
Write-Host "  2. To enforce the RULES.md/AGENTS.md contract every session, add to the"
Write-Host "     project's .claude/CLAUDE.md:"
Write-Host "       @../$Dir/RULES.md"
Write-Host "       @../$Dir/AGENTS.md"
Write-Host "  3. (Optional) For a persistent install without the flag, register $Dir as a"
Write-Host "     local plugin marketplace in .claude/settings.json."
