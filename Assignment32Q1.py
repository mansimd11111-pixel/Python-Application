import schedule
import time
from datetime import datetime

def CreateFile():
    filename = datetime.now().strftime("File_%d_%m_%Y_%H_%M_%S.txt")

    with open(filename, "w") as f:
        f.write("Filename : " + filename + "\n")
        f.write("Creation Date : " + datetime.now().strftime("%d-%m-%Y") + "\n")
        f.write("Creation Time : " + datetime.now().strftime("%I:%M:%S %p"))

    print(filename, "created.")

schedule.every(1).minutes.do(CreateFile)

while True:
    schedule.run_pending()
    time.sleep(1)