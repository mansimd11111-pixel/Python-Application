def DisplayFile(filename):
    file = open(filename, "r")
    for line in file:
        print(line, end="")
    file.close()

fname = input("Enter file name: ")
DisplayFile(fname)