import os
import sys

from utils import upload_files_to_db

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Run with default directory")
    else:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("Usage: python upload_documents.py <directory>")
            exit(0)
        directory = sys.argv[1]
        # Check if the argument is a directory
        if os.path.isdir(directory):
            # Check if the directory is empty
            if not os.listdir(directory):
                print("The directory is empty.")
            else:
                upload_files_to_db(sys.argv[1])
        else:
            print("The {0} is not a directory.".format(directory))
