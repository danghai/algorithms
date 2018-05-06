"""
List all directories in an absolute path
"""
import os
def enumerate_directory(path):
    # Check exist path
    if not os.path.exists(path):
        raise Exception("Path %s not exist" % path)
    directory_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dirs in dirnames:
            directory_collection.append(dirs)

    return directory_collection

if __name__ == "__main__":
    path_name = "/home"

    print("\nRecursive listing of all directory in a dir:")
    for dirs in enumerate_directory(path_name):
        print(dirs)
