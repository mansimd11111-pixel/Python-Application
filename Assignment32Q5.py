
import os
import schedule
import time

def DeleteEmptyFiles(path):
    with open("DeleteLog.txt","a") as log:
        for root, dirs, files in os.walk(path):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    if os.path.getsize(filepath) == 0:
                        os.remove(filepath)
                        log.write(filepath + " deleted\n")
                except PermissionError:
                    log.write(filepath + " permission denied\n")

    print("Task completed.")

path = input("Enter directory path: ")

schedule.every(1).hours.do(DeleteEmptyFiles, path)

while True:
    schedule.run_pending()
    time.sleep(1)