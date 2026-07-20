def CountLines(filename):
    file = open(filename,"r")
    count = 0
    for line in file:
        count += 1
    file.close()
    print("Total numbers of lines : ",count)
    
    
    fname = input("Enter file name: ")
    CountLines(fname)