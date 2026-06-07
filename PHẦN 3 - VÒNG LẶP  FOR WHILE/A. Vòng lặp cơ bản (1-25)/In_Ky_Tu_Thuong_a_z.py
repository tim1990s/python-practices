# Chương trình in ký tự a-z

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

for ma in range(ord("a"), ord("z") + 1):
    print(chr(ma))
