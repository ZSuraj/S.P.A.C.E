import csv
from functions import say

# Months list
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


class Birthday:
    def __init__(self) -> None:
        pass

    def add_birthday(name):
        name = name.replace("add", "").replace("birthday", "").replace("'s", "").strip()

        # if name not in the input ask the user input to add name to the csv
        if not name:
            say("What the name?")
            name = input("Name: ")

        # Birthday month
        say("what's the month")
        # If not a valid month prompt again
        while True:
            month = input("month: ")
            # Validate month
            if month not in months:
                say("That is not a month at all")
            else:
                break
        
        # Birthday date
        say("what's the date")
        # If not valid date prompt the user again
        while True:
            date = input("date: ")
            # Validate date
            if 0 <= int(date) <= 31:
                break
            else: 
                say("give me a valid date")
        
        bdate = month + date

        # Add the birthday to the csv file
        with open('birthday.csv', 'a', newline="") as file:
            f = ["Name", "Birthday"]
            bday_writer = csv.DictWriter(file, f)
            bday_writer.writerow({"Name" : name, "Birthday" : bdate})

        print("birthday added!!!")
        say("birthday added")
    
    def remind_birthday(phrase):
        phrase = phrase.replace("when is", "").replace("birthday", "").replace("'s", "").strip()

        with open('birthday.csv', 'r') as file:
            bday_reader = csv.DictReader(file)
            # Loop through read file
            for i in bday_reader:
                # if name matches the user input name
                # return the value
                if i["Name"] == phrase:
                    return i
