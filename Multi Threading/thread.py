import threading
import time

def print_num():
    for i in range(1,6):
        print(f"Number: {i}")
        time.sleep(0.7)

def print_letter():
    for i in ['A','B','C','D','E']:
        print(f"Letter: {i}")
        time.sleep(1.6)

def print_hello():
    for i in 'HELLO':
        print(f"Hello: {i}")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=print_num)
    t2 = threading.Thread(target=print_letter)
    t3 = threading.Thread(target=print_hello)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All Threads finished")

if __name__ == "__main__":
    main()