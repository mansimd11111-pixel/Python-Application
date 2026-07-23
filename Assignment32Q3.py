import os
import schedule
import time

def ReadFile(path):
    try:
        if not os.path.exists(path):
            print("File does not exist")
            return

        if os.path.getsize(path) == 0:
            print("File is empty.")
            return

        with open(path, "r") as f:
            print(f.read())

    except PermissionError:
        print("Permission denied")

    except Exception:
        print("File cannot be opened")

path = input("Enter file path:")

schedule.every(1).minutes.do(ReadFile, path)

while True:
    schedule.run_pending()
    time.sleep(1)