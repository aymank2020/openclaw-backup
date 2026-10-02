"""Check tracked paths without reading or printing any credential values."""
import pathlib
import subprocess
import sys

def main():
    result = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True)
    blocked = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        name = raw.decode("utf-8", "replace")
        item = pathlib.PurePosixPath(name.lower())
        if (item.parts[0] in {"config", "sessions", ".openclaw"}
                or item.suffix in {".sqlite", ".db", ".pem", ".key", ".zip"}
                or name.lower().endswith(".tar.gz")):
            blocked.append(name)
    if blocked:
        print("FAIL: private state paths are tracked (values were not read):")
        for name in blocked:
            print(name)
        return 1
    print("PASS: public tree contains no private OpenClaw state paths.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
