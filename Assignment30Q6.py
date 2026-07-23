import schedule
import time

def lunch():
    print("Lunch Time!")

def wrapup():
    print("Wrap up work")

schedule.every().day.at("13:00").do(lunch)
schedule.every().day.at("18:00").do(wrapup)

while True:
    schedule.run_pending()
    time.sleep(1)