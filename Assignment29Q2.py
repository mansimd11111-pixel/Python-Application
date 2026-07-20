fname = input("Enter file name: ")

fobj = open(fname,"r")
print(fobj.read())
fobj.close()