"""
List all files in an absolute path
"""
import os
def enumerate_file(path):
    # Check exist path
    if not os.path.exists(path):
        raise Exception("Path %s not exist" % path)
    file_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for files in filenames:
            file_collection.append(files)

    return file_collection

if __name__ == "__main__":
    path_name = "/home"
    print("\nRecursive listing of all files in a dir:")
    for files in enumerate_file(path_name):
        print(files)
