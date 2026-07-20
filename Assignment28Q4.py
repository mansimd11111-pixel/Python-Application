def CopyFile(source, destination):
    file1 = open(source, "r")
    data = file1.read()
    file1.close()

    file2 = open(destination, "w")
    file2.write(data)
    file2.close()

    print("Contents copied successfully.")

src = input("Enter source file: ")
dest = input("Enter destination file: ")
CopyFile(src, dest)