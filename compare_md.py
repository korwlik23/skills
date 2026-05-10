"""
📊 MD File Comparator — เปรียบเทียบไฟล์ .md ระหว่าง v1 กับ v2
==============================================================
ใช้งาน:
  python compare_md.py                         # เทียบทั้งหมด
  python compare_md.py SKILL.md                # เทียบเฉพาะไฟล์ชื่อ SKILL.md ทุกโฟลเดอร์
  python compare_md.py RULES.md                # เทียบเฉพาะ RULES.md
  python compare_md.py bug-debugging           # เทียบเฉพาะโฟลเดอร์ bug-debugging
  python compare_md.py bug-debugging SKILL.md  # เทียบเฉพาะ bug-debugging/SKILL.md
  python compare_md.py release-version testing-qa  # เทียบหลายโฟลเดอร์

ผลลัพธ์: แสดงรายการไฟล์ที่เหมือน/ต่างกัน พร้อมรายละเอียดจุดที่ต่าง
"""

from __future__ import annotations
import os
import difflib
import sys
import io
import fnmatch

# ── Fix Windows encoding (cp1252 → utf-8) ────────────────────
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ─── Configuration ────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
V1_DIR = os.path.join(SCRIPT_DIR, "v1")
V2_DIR = os.path.join(SCRIPT_DIR, "v2")

# ─── ANSI Colors ──────────────────────────────────────────────
class C:
    GREEN   = "\033[92m"
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    CYAN    = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"


def collect_md_files(base_dir: str) -> dict[str, str]:
    """รวบรวมไฟล์ .md ทั้งหมด คืนค่า {relative_path: absolute_path}"""
    md_files = {}
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.lower().endswith(".md"):
                abs_path = os.path.join(root, f)
                rel_path = os.path.relpath(abs_path, base_dir)
                md_files[rel_path] = abs_path
    return md_files


def filter_files(md_files: dict[str, str], filters: list[str]) -> dict[str, str]:
    """กรองไฟล์ตาม filter keywords
    
    รองรับ:
      - ชื่อไฟล์ตรงๆ เช่น "SKILL.md", "RULES.md"
      - ชื่อโฟลเดอร์ เช่น "bug-debugging", "release-version"
      - wildcard pattern เช่น "bug-*", "*.md"
      - path บางส่วน เช่น "bug-debugging/SKILL.md"
    """
    if not filters:
        return md_files

    filtered = {}
    for rel_path, abs_path in md_files.items():
        # แยก parts ของ path
        path_parts = rel_path.replace("\\", "/").split("/")
        filename = path_parts[-1]
        folder = path_parts[0] if len(path_parts) > 1 else ""

        for f in filters:
            f_normalized = f.replace("\\", "/")
            matched = False

            # 1. exact match กับ relative path
            if rel_path.replace("\\", "/") == f_normalized:
                matched = True
            # 2. exact match กับชื่อไฟล์
            elif filename.lower() == f.lower():
                matched = True
            # 3. exact match กับชื่อโฟลเดอร์
            elif folder.lower() == f.lower():
                matched = True
            # 4. substring match — keyword อยู่ใน path
            elif f.lower() in rel_path.lower():
                matched = True
            # 5. wildcard pattern match
            elif fnmatch.fnmatch(rel_path.lower(), f"*{f.lower()}*"):
                matched = True

            if matched:
                filtered[rel_path] = abs_path
                break

    return filtered


def read_file_lines(filepath: str) -> list[str]:
    """อ่านไฟล์แล้วคืนเป็น list ของบรรทัด"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.readlines()
    except Exception as e:
        print(f"  {C.RED}❌ อ่านไฟล์ไม่ได้: {filepath} — {e}{C.RESET}")
        return []


def show_diff(v1_lines: list[str], v2_lines: list[str], rel_path: str):
    """แสดง unified diff ของไฟล์ที่ต่างกัน"""
    diff = list(difflib.unified_diff(
        v1_lines, v2_lines,
        fromfile=f"v1/{rel_path}",
        tofile=f"v2/{rel_path}",
        lineterm=""
    ))

    if not diff:
        return

    for line in diff:
        line_stripped = line.rstrip("\n")
        if line_stripped.startswith("+++") or line_stripped.startswith("---"):
            print(f"  {C.BOLD}{C.CYAN}{line_stripped}{C.RESET}")
        elif line_stripped.startswith("@@"):
            print(f"  {C.MAGENTA}{line_stripped}{C.RESET}")
        elif line_stripped.startswith("+"):
            print(f"  {C.GREEN}{line_stripped}{C.RESET}")
        elif line_stripped.startswith("-"):
            print(f"  {C.RED}{line_stripped}{C.RESET}")
        else:
            print(f"  {C.DIM}{line_stripped}{C.RESET}")


def compare_files(v1_path: str, v2_path: str) -> bool:
    """เปรียบเทียบ 2 ไฟล์ คืน True ถ้าเหมือนกัน"""
    try:
        with open(v1_path, "rb") as f1, open(v2_path, "rb") as f2:
            return f1.read() == f2.read()
    except Exception:
        return False


def diff_two_files(path_a: str, path_b: str):
    """เปรียบเทียบ 2 ไฟล์โดยตรง (ไม่จำเป็นต้องอยู่ใน v1/v2)"""
    print()
    print(f"{C.BOLD}{'='*60}{C.RESET}")
    print(f"{C.BOLD}  📊 MD File Comparator — Direct Diff{C.RESET}")
    print(f"{C.BOLD}{'='*60}{C.RESET}")
    print()

    # ── ตรวจสอบว่าไฟล์มีจริง ──────────────────────────────
    for p in [path_a, path_b]:
        if not os.path.isfile(p):
            print(f"{C.RED}❌ ไม่พบไฟล์: {p}{C.RESET}")
            sys.exit(1)

    # ── เปรียบเทียบ ──────────────────────────────────────────
    is_same = compare_files(path_a, path_b)
    name_a = os.path.basename(path_a)
    name_b = os.path.basename(path_b)

    print(f"  {C.CYAN}A: {path_a}{C.RESET}")
    print(f"  {C.CYAN}B: {path_b}{C.RESET}")
    print()

    if is_same:
        print(f"{C.GREEN}{C.BOLD}✅ ไฟล์ทั้งสองเหมือนกันทุกประการ{C.RESET}")
    else:
        print(f"{C.RED}{C.BOLD}❌ ไฟล์ต่างกัน — รายละเอียด:{C.RESET}")
        print()
        a_lines = [l.rstrip("\n") for l in read_file_lines(path_a)]
        b_lines = [l.rstrip("\n") for l in read_file_lines(path_b)]

        diff = list(difflib.unified_diff(
            a_lines, b_lines,
            fromfile=f"A: {name_a}",
            tofile=f"B: {name_b}",
            lineterm=""
        ))

        for line in diff:
            line_stripped = line.rstrip("\n")
            if line_stripped.startswith("+++") or line_stripped.startswith("---"):
                print(f"  {C.BOLD}{C.CYAN}{line_stripped}{C.RESET}")
            elif line_stripped.startswith("@@"):
                print(f"  {C.MAGENTA}{line_stripped}{C.RESET}")
            elif line_stripped.startswith("+"):
                print(f"  {C.GREEN}{line_stripped}{C.RESET}")
            elif line_stripped.startswith("-"):
                print(f"  {C.RED}{line_stripped}{C.RESET}")
            else:
                print(f"  {C.DIM}{line_stripped}{C.RESET}")

    print()


def print_usage():
    """แสดงวิธีใช้"""
    print(f"""
{C.BOLD}วิธีใช้:{C.RESET}

  {C.BOLD}โหมด 1: เทียบ v1 vs v2{C.RESET}
  python compare_md.py                              {C.DIM}# เทียบทั้งหมด{C.RESET}
  python compare_md.py SKILL.md                     {C.DIM}# เทียบเฉพาะ SKILL.md ทุกโฟลเดอร์{C.RESET}
  python compare_md.py RULES.md                     {C.DIM}# เทียบเฉพาะ RULES.md{C.RESET}
  python compare_md.py bug-debugging                {C.DIM}# เทียบทุกไฟล์ในโฟลเดอร์ bug-debugging{C.RESET}
  python compare_md.py bug-debugging SKILL.md       {C.DIM}# เทียบ bug-debugging/SKILL.md{C.RESET}
  python compare_md.py release-version testing-qa   {C.DIM}# เทียบหลายโฟลเดอร์{C.RESET}

  {C.BOLD}โหมด 2: เทียบ 2 ไฟล์โดยตรง{C.RESET}
  python compare_md.py --diff fileA.md fileB.md     {C.DIM}# เทียบ 2 ไฟล์อะไรก็ได้{C.RESET}
  python compare_md.py --diff v1/RULES.md "v1/RULES 1.md"  {C.DIM}# ตัวอย่างจริง{C.RESET}

  python compare_md.py --help                       {C.DIM}# แสดงวิธีใช้{C.RESET}
""")


def main():
    # ── ตรวจสอบ --help ──────────────────────────────────────
    args = sys.argv[1:]
    if "--help" in args or "-h" in args:
        print_usage()
        sys.exit(0)

    # ── โหมด --diff: เทียบ 2 ไฟล์โดยตรง ─────────────────────
    if "--diff" in args:
        idx = args.index("--diff")
        remaining = args[idx + 1:]
        if len(remaining) < 2:
            print(f"{C.RED}❌ --diff ต้องระบุ 2 ไฟล์{C.RESET}")
            print(f"{C.DIM}ตัวอย่าง: python compare_md.py --diff v1/RULES.md \"v1/RULES 1.md\"{C.RESET}")
            sys.exit(1)
        diff_two_files(remaining[0], remaining[1])
        sys.exit(0)

    filters = args  # อาจเป็น list ว่าง (= เทียบทั้งหมด)

    print()
    print(f"{C.BOLD}{'='*60}{C.RESET}")
    print(f"{C.BOLD}  📊 MD File Comparator — v1 vs v2{C.RESET}")
    print(f"{C.BOLD}{'='*60}{C.RESET}")

    if filters:
        print(f"  {C.CYAN}🔍 ค้นหา: {', '.join(filters)}{C.RESET}")

    print()

    # ── ตรวจสอบว่า directory มีจริง ────────────────────────
    if not os.path.isdir(V1_DIR):
        print(f"{C.RED}❌ ไม่พบ directory: {V1_DIR}{C.RESET}")
        sys.exit(1)
    if not os.path.isdir(V2_DIR):
        print(f"{C.RED}❌ ไม่พบ directory: {V2_DIR}{C.RESET}")
        sys.exit(1)

    # ── รวบรวมไฟล์ .md ──────────────────────────────────────
    v1_files = collect_md_files(V1_DIR)
    v2_files = collect_md_files(V2_DIR)

    # ── กรองตาม filter (ถ้ามี) ──────────────────────────────
    if filters:
        v1_files = filter_files(v1_files, filters)
        v2_files = filter_files(v2_files, filters)

    all_paths = sorted(set(v1_files.keys()) | set(v2_files.keys()))

    if not all_paths:
        if filters:
            print(f"{C.YELLOW}⚠️  ไม่พบไฟล์ .md ที่ตรงกับ: {', '.join(filters)}{C.RESET}")
            print()
            print(f"{C.DIM}ลองใช้ --help เพื่อดูวิธีใช้งาน{C.RESET}")
        else:
            print(f"{C.YELLOW}⚠️  ไม่พบไฟล์ .md ใน v1 หรือ v2{C.RESET}")
        sys.exit(0)

    # ── ตัวนับสถิติ ──────────────────────────────────────────
    identical = []
    different = []
    only_v1   = []
    only_v2   = []

    # ── เปรียบเทียบทีละไฟล์ ──────────────────────────────────
    for rel_path in all_paths:
        in_v1 = rel_path in v1_files
        in_v2 = rel_path in v2_files

        if in_v1 and not in_v2:
            only_v1.append(rel_path)
        elif in_v2 and not in_v1:
            only_v2.append(rel_path)
        elif compare_files(v1_files[rel_path], v2_files[rel_path]):
            identical.append(rel_path)
        else:
            different.append(rel_path)

    # ── แสดงผลไฟล์ที่เหมือนกัน ───────────────────────────────
    if identical:
        print(f"{C.GREEN}{C.BOLD}✅ ไฟล์ที่เหมือนกัน ({len(identical)} ไฟล์):{C.RESET}")
        for p in identical:
            print(f"   {C.GREEN}• {p}{C.RESET}")
        print()

    # ── แสดงผลไฟล์ที่มีแค่ใน v1 ──────────────────────────────
    if only_v1:
        print(f"{C.YELLOW}{C.BOLD}📁 มีเฉพาะใน v1 ({len(only_v1)} ไฟล์):{C.RESET}")
        for p in only_v1:
            print(f"   {C.YELLOW}• {p}{C.RESET}")
        print()

    # ── แสดงผลไฟล์ที่มีแค่ใน v2 ──────────────────────────────
    if only_v2:
        print(f"{C.CYAN}{C.BOLD}📁 มีเฉพาะใน v2 ({len(only_v2)} ไฟล์):{C.RESET}")
        for p in only_v2:
            print(f"   {C.CYAN}• {p}{C.RESET}")
        print()

    # ── แสดงผลไฟล์ที่ต่างกัน พร้อม diff ──────────────────────
    if different:
        print(f"{C.RED}{C.BOLD}❌ ไฟล์ที่ต่างกัน ({len(different)} ไฟล์):{C.RESET}")
        print()
        for p in different:
            print(f"  {C.BOLD}{C.RED}── {p} ──{C.RESET}")
            v1_lines = [l.rstrip("\n") for l in read_file_lines(v1_files[p])]
            v2_lines = [l.rstrip("\n") for l in read_file_lines(v2_files[p])]
            show_diff(v1_lines, v2_lines, p)
            print()

    # ── สรุป ─────────────────────────────────────────────────
    print(f"{C.BOLD}{'='*60}{C.RESET}")
    print(f"{C.BOLD}  📋 สรุป{C.RESET}")
    print(f"{C.BOLD}{'='*60}{C.RESET}")
    total = len(all_paths)
    print(f"   ไฟล์ทั้งหมด       : {total}")
    print(f"   {C.GREEN}✅ เหมือนกัน       : {len(identical)}{C.RESET}")
    print(f"   {C.RED}❌ ต่างกัน         : {len(different)}{C.RESET}")
    print(f"   {C.YELLOW}📁 มีเฉพาะ v1     : {len(only_v1)}{C.RESET}")
    print(f"   {C.CYAN}📁 มีเฉพาะ v2     : {len(only_v2)}{C.RESET}")
    print()


if __name__ == "__main__":
    main()
