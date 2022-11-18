import re
import os
import smtplib
import csv

# Environment variables
my_email = os.environ.get("SPACE_EMAIL_ID")
my_pass = os.environ.get("SPACE_APP_PASSWORD")

class Email:
    def __init__(self):
        pass

    def main(string):

        to = None

        # Reading file as a dictionary
        with open('email_ids.csv','r') as file:
            email_ids = csv.DictReader(file)

            # Extracting the user input
            try:
                regex = r"to (.*)"
                match = re.findall(regex, string) 
                person = match[0]

            except IndexError:
                try:   
                    regex = r"send (\w+ \w+)"
                    match = re.findall(regex, string) 
                    person = match[0]
            
                except IndexError:
                    regex = r"send (\w+)"
                    match = re.findall(regex, string) 
                    person = match[0]
            
            # Looping through the dictionary
            for i in email_ids:

                # If user input name matches one of the names in the dictionary
                if person == i["Name"]:
                    to = i["Email id"]

            # If no matches from the dictionary
            # Prompt the user for recipient's email id
            if to == None: 
                to = input("email id: ")

                # Add it to the csv
                with open('email_ids.csv','a', newline="") as file:
                    f = ["Name", "Email id"]
                    write_email = csv.DictWriter(file, f)
                    write_email.writerow({"Name" : person, "Email id" : to})

        return person, to


    def send_email(to, content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(my_email, my_pass)
        server.sendmail(my_email, to, content)
        server.close()
            