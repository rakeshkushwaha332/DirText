import os

def scan_folder_recursive(folder_path, output_file="folder_info.txt"):
    """
    Recursively scans a given folder and writes the folder structure, subfolder count, 
    and file count into a text file.

    :param folder_path: The root folder to scan.
    :param output_file: The name of the text file to store the results.
    """
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Scanning folder: {folder_path}\n")
        file.write("=" * 70 + "\n\n")

        for root, subdirs, files in os.walk(folder_path):
            # Compute indentation level for better readability
            indent_level = root.replace(folder_path, "").count(os.sep)
            indent = "    " * indent_level  # Indentation for hierarchy
            
            file.write(f"{indent}📁 Folder: {root}\n")
            file.write(f"{indent}  - Contains {len(subdirs)} subfolders\n")
            file.write(f"{indent}  - Contains {len(files)} files\n")

            # Write subfolder names
            if subdirs:
                file.write(f"{indent}  Subfolders:\n")
                for subdir in subdirs:
                    file.write(f"{indent}    📂 {subdir}\n")

            # Write file names
            if files:
                file.write(f"{indent}  Files:\n")
                for filename in files:
                    file.write(f"{indent}    📄 {filename}\n")

            file.write("\n" + "-" * 70 + "\n\n")

    print(f"Folder scan completed. Data saved in '{output_file}'")


# Example usage
folder_path = input("Enter the path of the folder to scan: ")
scan_folder_recursive(folder_path)
