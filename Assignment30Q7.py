import schedule
import time
import shutil
import os
from datetime import datetime

source = input("Enter source file path: ")
destination = input("Enter destination folder path: ")

def backup():
    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)

    newname = name + "" + datetime.now().strftime("%d%m_%Y_%H_%M_%S") + ext
    destfile = os.path.join(destination, newname)

    shutil.copy(source, destfile)

    with open("backup_log.txt","a") as f:
        f.write("Backup completed successfully at " +
                datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    print("Backup Completed")

schedule.every(1).hours.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)