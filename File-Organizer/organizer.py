
import os
import shutil
from pathlib import Path

# Step 1: Define file categories
extension_map = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}

# Step 2: Handle duplicate filenames
def get_unique_path(destination):

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            destination.stem + "_" +
            str(counter) + destination.suffix
        )

        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


# Step 3: Get folder path
print("\n===================================")
print("       AUTOMATIC FILE ORGANIZER")
print("===================================")

folder_path = input("\nEnter folder path: ").strip().strip('"')

folder = Path(folder_path)

if not folder.exists() or not folder.is_dir():
    print("Invalid folder path!")
    raise SystemExit

# Step 4: Initialize counters
total_moved = 0
total_skipped = 0
total_errors = 0

# Step 5: Scan directory and subdirectories
directories = [folder]

while directories:

    current_folder = directories.pop()

    try:
        with os.scandir(current_folder) as entries:

            for entry in entries:

                try:
                    if entry.is_symlink():
                        total_skipped += 1
                        continue

                    if entry.is_dir():
                        # Do not scan category folders at root
                        if current_folder == folder and entry.name in set(extension_map.values()) | {"Others"}:
                            continue

                        directories.append(Path(entry.path))
                        continue

                    if not entry.is_file():
                        continue

                    file_path = Path(entry.path)

                    # Step 6: Identify file category
                    extension = file_path.suffix.lower()

                    category = extension_map.get(
                        extension, "Others"
                    )

                    # Step 7: Create destination folder
                    destination_folder = folder / category
                    destination_folder.mkdir(exist_ok=True)

                    # Step 8: Move without overwriting
                    destination = get_unique_path(
                        destination_folder / file_path.name
                    )

                    try:
                        shutil.move(
                            str(file_path),
                            str(destination)
                        )

                    except FileExistsError:
                        # Choose another name if a collision occurs
                        destination = get_unique_path(
                            destination_folder / file_path.name
                        )

                        shutil.move(
                            str(file_path),
                            str(destination)
                        )

                    print(
                        "Moved:", file_path.name,
                        "->", category
                    )

                    total_moved += 1

                except PermissionError:
                    print("Permission denied:", entry.name)
                    total_errors += 1

                except OSError as error:
                    print("File error:", entry.name, error)
                    total_errors += 1

    except PermissionError:
        print("Cannot access folder:", current_folder)
        total_errors += 1

    except OSError as error:
        print("Folder error:", error)
        total_errors += 1

# Step 9: Display final summary
print("\n===================================")
print("       ORGANIZATION SUMMARY")
print("===================================")

print("Total files moved:", total_moved)
print("Total files skipped:", total_skipped)
print("Total errors:", total_errors)

print("\nFile organization completed!")
