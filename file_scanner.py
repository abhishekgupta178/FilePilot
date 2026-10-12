
from pathlib import Path


def scan_files(folder):
    path = Path(folder)

    if not path.is_dir():
        raise ValueError("Please select a valid folder.")

    return [
        item for item in path.iterdir()
        if item.is_file()
    ]
