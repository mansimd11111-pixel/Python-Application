import schedule
import time

def MondayMessage():
    print("Start your weekly goals")

def WednesdayMessage():
    print("Review your weekly progress")

def FridayMessage():
    print("Weekly work completed")

schedule.every().monday.at("09:00").do(MondayMessage)
schedule.every().wednesday.at("17:00").do(WednesdayMessage)
schedule.every().friday.at("18:00").do(FridayMessage)

while True:
    schedule.run_pending()
    time.sleep(1)