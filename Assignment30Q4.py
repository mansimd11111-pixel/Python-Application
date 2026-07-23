import schedule
import time

def greet():
    print("Namaskar...")

schedule.every().day.at("09:00").do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)