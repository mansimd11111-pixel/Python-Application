import schedule
import time

def message():
    print("Coding Kar..!")

schedule.every(30).minutes.do(message)

while True:
    schedule.run_pending()
    time.sleep(1)