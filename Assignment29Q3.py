import sys

source = sys.argv[1]

f1 = open(source,"r")
data = f1.read()
f1.close()

f2 = open("Demo.txt","w")
f2.write(data)
f2.close()

print("Contents copied successfully.")