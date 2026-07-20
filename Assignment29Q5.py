fname = input("Enter file name: ")
word = input("Enter string: ")

fobj = open(fname,"r")
data = fobj.read()
fobj.close()

count = data.count(word)

print("Frequency of",word,"is",count)