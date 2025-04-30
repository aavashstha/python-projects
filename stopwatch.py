import time
import math

def stopwatch():


    for seconds in range(stopwatch_time, 0, -1):
        
        hours = math.floor(seconds / 3600)
        minutes = math.floor(seconds / 60) % 60
        seconds = seconds % 60



        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("TIME'S UP!📣")

while True:
    stopwatch_time = input("Enter time in seconds (q to quit): ")
    if stopwatch_time.lower() == "q":
        print("BYE!👋")
        break
    elif stopwatch_time.isdigit():
        stopwatch_time = int(stopwatch_time)
        stopwatch()
        continue
    else:
        print("INVALID INPUT!")
        continue