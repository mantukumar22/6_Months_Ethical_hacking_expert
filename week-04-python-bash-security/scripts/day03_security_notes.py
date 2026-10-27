from pathlib import Path

file_path = Path("findings.txt")

try:
    file_path.write_text(
        "Finding: Missing security header\n",
        encoding="utf-8",
    )
    content = file_path.read_text(encoding="utf-8")
    print(content)
except OSError as error:
    print("File operation failed:", error)

# TODO: try making the path unwritable (e.g. a folder that doesn't exist)
# and watch the except branch run. Then add logging:
#   import logging
#   logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
