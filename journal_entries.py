import os 
from datetime import datetime

journal_dir = "Journal Entries"
if not os.path.exists(journal_dir):
    os.mkdir(journal_dir)

def get_today_filename():
   return f"{journal_dir}/{datetime.now().strftime('%d-%m-%y')}.txt"

def new_entry():
    filename = get_today_filename()
    if os.path.exists(filename):
        print("Warning : Todays Jouranl Already exists. Overwriting..!")
    entry_date = input("Enter Date of Entry: ")
    entry_mood = input("Enter Your Today Mood: ")
    entry_thought = input("Enter Your Today Thought: ")
    entry_learn = input("Enter Your Today Learning: ")

    entry_data = (
        f"Date      : {entry_date}\n"
        f"Mood      : {entry_mood}\n"
        f"Thought   : {entry_thought}\n"
        f"Learning  : {entry_learn}\n"
    )


    with open(filename,'a') as file:
        file.write(entry_data)
    print(f"File Saved as {filename}")

def enter_filename():
    filename = input("Enter filename in DD-MM-YY format (without .txt): ")
    return f"Journal Entries/{filename}.txt"

def read_entry():
    file_path = enter_filename()
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            print(file.read())
    else:
        print(f"{file_path} does not exist.")


def remove_entry():
    file_path = enter_filename()
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted !")
    else:
        print(f"{file_path} does not exist .")

while True:
    try:
        choice = int(input(" \n 1. Create File\n 2. Read File\n 3. Remove File\n 4. Exit\n \nEnter Your choice:"))
        match choice:
            case 1:
                new_entry()
            case 2: 
                read_entry()
            case 3:
                remove_entry()
            case 4:
                print("Exiting Journal App")
                break
            case _:
                print("Invalid Choice !...Try Again")
    except:
        print("Please Enter a valid number !")