import os
import schedule
import time
from datetime import datetime

def MonitorFile(path):
    if os.path.exists(path):
        size = os.path.getsize(path)

        with open("FileSizeLog.txt", "a") as f:
            f.write(f"File Path : {path}\n")
            f.write(f"File Size : {size} bytes\n")
            f.write(f"Date & Time : {datetime.now()}\n")
            f.write("-"*40 + "\n")

        print("Log Updated")
    else:
        print("File does not exist.")

path = input("Enter file path: ")

schedule.every(30).seconds.do(MonitorFile, path)

while True:
    schedule.run_pending()
    time.sleep(1)