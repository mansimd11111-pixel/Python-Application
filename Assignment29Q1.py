import os

fname = input("Enter file name: ")

if os.path.exists(fname):
    print(fname,"exists.")
else:
    print(fname,"does not exist")