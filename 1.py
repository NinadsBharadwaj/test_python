import os
import sys
import pathlib
import zipfile

dirname=input("Enter Dir")
if not os.path.isdir(dirname):
    print("dir not found")
    sys.exit(0)
curdirectory=pathlib.Path(dirname)
with zipfile.ZipFile("backup.zip",mode="w")as archive:
    for file_path in curdirectory.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curdirectory))
if os.path.isfile("backup.zip"):
    print("Succ")
else:
    print("no")