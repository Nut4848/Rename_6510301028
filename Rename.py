import os

def rename_files(directory, file_extension):

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    filtered_files = [f for f in files if f.endswith(file_extension)]

    filtered_files.sort()

    counter = 1

    for old_filename in filtered_files:
        new_filename = f"{counter:03d}{file_extension}"
        old_path = os.path.join(directory, old_filename)
        new_path = os.path.join(directory, new_filename)

        while os.path.exists(new_path):
            counter += 1
            new_filename = f"{counter:03d}{file_extension}"
            new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {old_filename} -> {new_filename}")

        counter += 1

directory_path = r"C:\Users\Asus\Desktop\directory"
file_extension_to_rename = ".jpg"
rename_files(directory_path, file_extension_to_rename)


