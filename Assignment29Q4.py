import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

f1 = open(file1,"r")
f2 = open(file2,"r")

if f1.read() == f2.read():
    print("Success")
else:
    print("Failure")

f1.close()
f2.close()