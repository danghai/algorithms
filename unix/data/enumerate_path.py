"""
List all file paths in an absolute path
"""
import os
def enumerate_path(path):
    # Check exist path
    if not os.path.exists(path):
        raise Exception("Path %s not exist" % path)
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for files in filenames:
            fullpath = os.path.join(dirpath, files)
            path_collection.append(fullpath)

    return path_collection

if __name__ == "__main__":
    path_name = "/home"
    print("\nRecursive listing of all paths in a dir:")
    for path in enumerate_path(path_name):
        print(path)
