import os
import schedule
import time
from datetime import datetime

def CountFiles(path):
    count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    with open("DirectoryCountLog.txt", "a") as f:
        f.write(f"Directory: {path}\n")
        f.write(f"Files: {count}\n")
        f.write(f"Date & Time: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
        f.write("-" * 40 + "\n")

    print("Log updated.")

path = input("Enter directory path: ")

schedule.every(5).minutes.do(CountFiles, path)

while True:
    schedule.run_pending()
    time.sleep(1)