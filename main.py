import os
import shutil


def main_menu():
    while True:
        print("Python System Utils")
        print("==== Main Menu ====")
        print("1. Organize Files by Extension")
        print("2.Convert CSV To JSON")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # TODO
            organize_files_by_extension()
        elif choice == "2":
            # TODO
            pass
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def organize_files_by_extension():
    # TODO
    extensions = {
        "jpg": "images",
        "png": "images",
        "ico": "images",
        "gif": "images",
        "svg": "images",
        "sql": "sql",
        "exe": "programs",
        "msi": "programs",
        "pdf": "pdf",
        "xlsx": "excel",
        "csv": "excel",
        "rar": "archive",
        "zip": "archive",
        "gz": "archive",
        "tar": "archive",
        "docx": "word",
        "torrent": "torrent",
        "txt": "text",
        "ipynb": "python",
        "py": "python",
        "pptx": "powerpoint",
        "ppt": "powerpoint",
        "mp3": "audio",
        "wav": "audio",
        "mp4": "video",
        "m3u8": "video",
        "webm": "video",
        "ts": "video",
        "json": "json",
        "css": "web",
        "js": "web",
        "html": "web",
        "apk": "apk",
        "sqlite3": "sqlite3",
    }

    print("Organizing files by extension...")
    list_2 = os.listdir(os.getcwd())
    extension = []
    for val in list_2:
        if "." in val:
            extension.append(val.split(".")[1])
        for ext in extension:
            if ext in extensions.keys():
                folder = os.path.join(os.getcwd(), extensions.get(ext))
                os.mkdir(folder)
                shutil.move(os.path.join(os.getcwd(), val), os.path.join(folder, val))


if __name__ == "__main__":
    main_menu()
