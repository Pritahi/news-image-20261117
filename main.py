import os
import shutil
import hashlib
import sys

def get_hash(path):
    with open(path, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

def main():
    source = "entry.png"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, source)

    if not os.path.isfile(source):
        print(f"Error: {source} is missing", file=sys.stderr)
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)
    shutil.copy2(source, target)

    if os.path.getsize(source) != os.path.getsize(target) or get_hash(source) != get_hash(target):
        print("Error: Copy verification failed (not byte-identical)", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
