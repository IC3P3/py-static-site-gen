import os
import shutil


def copy_static_content(origin, dest):
    clear_generated_files(dest)

    print(f"Copying static files from {origin} to {dest}")
    copy_files(origin, dest)


def copy_files(orig, dest):
    entries = os.listdir(orig)

    if not os.path.exists(dest):
        os.mkdir(dest)

    for entry in entries:
        src_path = os.path.join(orig, entry)
        dest_path = os.path.join(dest, entry)

        if os.path.isfile(src_path):
            print(f" * {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            copy_files(src_path, dest_path)


def clear_generated_files(dest):
    if os.path.exists(dest):
        print(f"Deleting old files in: {dest}")
        shutil.rmtree(dest)

    print(f"Creating empty directory: {dest}")
    os.mkdir(dest)
