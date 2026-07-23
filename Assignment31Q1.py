import schedule
import time

def DisplayMessage(msg):
    print(msg)

message = input("Enter message: ")
interval = int(input("Enter interval in seconds: "))

if interval <= 0:
    print("Interval must be greater than zero.")
    exit()

schedule.every(interval).seconds.do(DisplayMessage, message)

while True:
    schedule.run_pending()
    time.sleep(1)