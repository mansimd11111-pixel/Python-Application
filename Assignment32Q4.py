import os
import shutil
import schedule
import time

def CopyFiles(src, dest):
    if not os.path.isdir(src) or not os.path.isdir(dest):
        print("Invalid directory.")
        return

    with open("CopyLog.txt", "a") as log:
        for file in os.listdir(src):
            if file.endswith(".txt"):
                try:
                    shutil.copy(os.path.join(src, file), dest)
                    log.write(file + "copied\n")
                except Exception:
                    log.write(file + "not copied\n")

    print("Copy completed.")

src = input("Enter source directory:")
dest = input("Enter destination directory:")

schedule.every(10).minutes.do(CopyFiles, src, dest)

while True:
    schedule.run_pending()
    time.sleep(1)