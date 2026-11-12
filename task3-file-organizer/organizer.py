import os
import shutil
from pathlib import Path

def get_unique_path(destination_path):
    """If a file with the same name exists, return name_1.ext, name_2.ext, ..."""
    if not os.path.exists(destination_path):
        return destination_path
    base, ext = os.path.splitext(destination_path)
    counter = 1
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    return f"{base}_{counter}{ext}"

def organize_directory(target_path):
    # 1. Create extension mapping dictionary
    EXTENSION_MAP = {
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.jpg': 'Images',
        '.png': 'Images',
        '.mp4': 'Videos',
        '.zip': 'Archives',
        '.py': 'Code',
        '.cs': 'Code',
        '.js': 'Code'
    }

    if not os.path.exists(target_path):
        print(f"[!] Error: The directory '{target_path}' does not exist.")
        return

    print(f"Scanning directory: {target_path}...\n")

    moved_count = 0
    error_count = 0
    renamed_count = 0

    # 2. Use os.scandir() for better performance
    with os.scandir(target_path) as entries:
        for entry in list(entries):
            # Process files only, skip directories
            if entry.is_file():
                file_path = Path(entry.path)
                file_ext = file_path.suffix.lower()

                # Determine category or default to 'Others'
                category = EXTENSION_MAP.get(file_ext, 'Others')
                category_folder = os.path.join(target_path, category)

                # Create category subfolder dynamically if it doesn't exist
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                destination_path = os.path.join(category_folder, entry.name)

                # Naming collision: rename instead of overwriting
                final_path = get_unique_path(destination_path)
                was_renamed = final_path != destination_path

                # 3. Use shutil.move() with Exception Handling
                try:
                    shutil.move(entry.path, final_path)
                    if was_renamed:
                        print(f"[+] Moved (renamed): {entry.name} -> {category}/{os.path.basename(final_path)}")
                        renamed_count += 1
                    else:
                        print(f"[+] Moved: {entry.name} -> {category}/")
                    moved_count += 1
                except FileExistsError:
                    print(f"[-] Error: '{entry.name}' already exists in {category}/. (FileExistsError)")
                    error_count += 1
                except PermissionError:
                    print(f"[-] Error: Permission denied for '{entry.name}'. It might be open in another program. (PermissionError)")
                    error_count += 1
                except Exception as e:
                    print(f"[-] Unexpected Error moving '{entry.name}': {e}")
                    error_count += 1

    # 4. Print Formatted Execution Summary
    print("\n" + "="*40)
    print("           EXECUTION SUMMARY ")
    print("="*40)
    print(f"Total files successfully relocated : {moved_count}")
    print(f"Total files renamed (collisions)   : {renamed_count}")
    print(f"Total files skipped due to errors  : {error_count}")
    print("="*40)

if __name__ == "__main__":
    # Take target directory input from the user
    folder_to_organize = input("Enter the directory path to organize (e.g., C:\\Users\\Tahmina\\Downloads): ")
    organize_directory(folder_to_organize)
