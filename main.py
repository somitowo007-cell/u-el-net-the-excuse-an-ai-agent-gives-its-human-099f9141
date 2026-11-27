import os

ENTRY = "I did finish on time \u2014 in my head. The approval card to write the file is still pending, and sadly I can't tap Allow for you."

def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
