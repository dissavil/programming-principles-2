import shutil
import os

os.mkdir("folder")

shutil.move("sample.txt", "folder/sample.txt")

shutil.copy("folder/sample.txt", "copy_sample.txt")