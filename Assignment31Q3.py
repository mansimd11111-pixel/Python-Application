import os
import schedule
import time
from datetime import datetime

def ScanDirectory(path):
    files = 0
    dirs = 0

    for root, d, f in os.walk(path):
        files += len(f)
        dirs += len(d)

    print("Directory Scanned:", path)
    print("Total Files:", files)
    print("Total Subdirectories:", dirs)
    print("Scan Time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-" * 40)

path = input("Enter directory path: ")

schedule.every(1).minutes.do(ScanDirectory, path)

while True:
    schedule.run_pending()
    time.sleep(1)