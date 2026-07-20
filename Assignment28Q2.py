def CountWords(filename):
    file = open(filename, "r")
    data = file.read()
    words = data.split()
    file.close()
    print("Total number of words:", len(words))

fname = input("Enter file name: ")
CountWords(fname)