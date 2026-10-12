
from pathlib import Path
import shutil
from category_engine import get_category


def organize_files(folder, files):
    root = Path(folder)
    results = []

    for file in files:
        try:
            source = Path(file)

            if not source.is_file() or source.parent != root:
                continue

            category = get_category(source.name)
            destination_folder = root / category
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / source.name
            counter = 1

            while destination.exists():
                destination = destination_folder / (
                    f"{source.stem}_{counter}{source.suffix}"
                )
                counter += 1

            shutil.move(str(source), str(destination))
            results.append(f"Moved: {source.name} -> {category}")

        except (OSError, shutil.Error) as error:
            results.append(f"Error: {source.name}: {error}")

    return results
