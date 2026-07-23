import schedule
import time
from datetime import datetime

def show_datetime():
    now = datetime.now()
    print("Current Date and Time:",now.strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(1).minutes.do(show_datetime)

while True:
    schedule.run_pending()
    time.sleep(1)