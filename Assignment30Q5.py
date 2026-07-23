import schedule
import time
from datetime import datetime

def write_file():
    with open("Marvellous.txt","a") as f:
        f.write("Task executed at: " +
                datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    print("Entry Added")

schedule.every(5).minutes.do(write_file)

while True:
    schedule.run_pending()
    time.sleep(1)