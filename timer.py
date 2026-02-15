import threading
import time

def stopwatch():
    seconds = 0
    while True:
        time.sleep(1)
        seconds += 1
        print(f"___________________Stopwatch: {seconds} Sec")

def countdown_timer(duration):
    for i in range(duration,0 ,-1):
        print(f"Timer: {i} sec left")
        time.sleep(1)
    print("Timer Finished..!")

def main():
    duration = int(input("Enter Countdown in second: "))

    t1 = threading.Thread(target=stopwatch,daemon=True)
    t2 = threading.Thread(target=countdown_timer,args=(duration,))
    t1.start()
    t2.start()

    t2.join()


if __name__ == "__main__":
    main()