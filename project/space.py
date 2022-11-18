import csv
import webbrowser
import wikipedia
import re
import pyjokes
from emails import Email
import random
from birthday import Birthday
from contacts import PhoneNumber
from holiday import show_holiday
from functions import say, listen, greet, date, time, get_random_advice, google_search

list = ["It's been wonderful! thanks.", "It's been great. how about you?.", "Really good! Thanks for asking", "Good. How was yours?", "Same old same old. How was yours?", "Any day is great when I am assisting you."]

job = ["My job is to make your job easier. I hope I'm doing a good job, you have a lot on your plate!", "I'm your virtual assistant, that means I can find info, get stuff done, and my favourite part:HAVE FUN 🙂", "I have the best job for an assistant, helping you. What can i do for you 😁"]

try:
    def main():

        greet()

        while (True):

            # Listen
            phrase = listen().lower()

            # Use user input
            # Using re module
            # Greet user using their name
            matches = re.search("my name is (\w+)", phrase)
            matches_1 = re.search("i am (\w+)", phrase)
            if matches_1:
                    matches = matches_1

            # Respond to user
            matches_2 = re.search("how are you", phrase)

            matches_3 = re.search("how was your day", phrase)

            matches_4 = re.search("what do you do", phrase)
            matches_5 = re.search("what is your job", phrase)
            
            # Search Web
            web = re.search("open (.*)", phrase)

            # Add and remind birthday
            add_birthday = re.search("add (\w+) birthday", phrase)
            remind_birthday = re.search("when is (\w+) birthday", phrase)
            
            # Add and show contacts
            add_phone_number = re.search("add (\w+) phone number", phrase)
            show_phone_number = re.search("show (\w+) phone number", phrase)
            

            # Call name
            if matches and matches_2:
                print(f"Hey {matches[1]}, how was your day?. I am fine, thanks")
                say(f"Hey {matches[1]}, how was your day?. I am fine, thanks")
                continue

            elif matches:
                print(f"Hey {matches[1]}, how was your day?")
                say(f"Hey {matches[1]}, how was your day?")
                continue
            
            # Responses 
            elif matches_2:
                print("I am fine, thanks")
                say("I am fine, thanks")
                continue
            
            elif matches_3:
                match = random.choice(list)
                print(match)
                say(match)
                continue
            
            elif matches_4 or matches_5:
                match = random.choice(job)
                print(match)
                say(match)
                continue
            
            # Search in youtube
            elif "on youtube" in phrase or "in youtube" in phrase:
                word = phrase.replace("search", "").replace("on youtube", "").replace("in youtube", "")
                print(f"opening {word} on youtube...")
                say(f"opening {word} on youtube...")
                webbrowser.open(f"https://www.youtube.com/results?search_query={word}")
                exit()

            # Open web
            elif web:
                open_web = phrase.replace("open", "").strip()
                say (f"opening {open_web}")
                print(f"opening {open_web}")
                webbrowser.open(f"{open_web}.com") 
                continue
            
            # Date
            elif "what date" in phrase:
                date()
                continue

            # Time
            elif "what time" in phrase:
                time()
                continue

            # Intro
            elif "what is your name" in phrase or "who are you" in phrase:
                say("My name is Space. I am a assistant")
                continue

            # Jokes
            elif "joke" in phrase:
                say("Here is a joke")
                x = pyjokes.get_joke()
                print(x)
                say(x)
                continue

            # Wikipedia search
            elif "who is" in phrase or "what is" in phrase or "where is" in phrase:
                try:
                    say("Searching wikipedia")
                    p = phrase.replace('who is', "").replace('what is', "").replace('where is', "")
                    x = wikipedia.summary(p, 2)
                    say("According to wikipedia")
                    print(x)
                    say(x)
                except wikipedia.exceptions.DisambiguationError:
                    print(f"Huh? Which {p} exactly?")
                    say(f"Which {p} exactly?")
                    continue
                except wikipedia.exceptions.WikipediaException:
                    print("Bro, say it again")
                    say("Bro, say it again")
                    continue

            # Advice
            elif "advice" in phrase:
                say(f"Here's a piece of advice for you")
                get_random_advice()
                continue

            # Email
            elif "email" in phrase:
                
                # from email import Email class
                # Extract person's name and email address 
                person, to = Email.main(phrase)

                # To get the content or body of email
                say(f"What should i say to {person}")
                content = listen().capitalize()
                
                # Sending email
                # send_email function defined in Email class, emails.py file
                Email.send_email(to, content)
                print("Email Sent")
                say("email sent")
                continue
            
            # Birthday

            # Add birthday
            elif add_birthday or "add birthday" in phrase:
    
                # add_birthday function defined in Birthday class, birthday.py file
                Birthday.add_birthday(phrase)
                continue
            
            # Remind birthday
            elif remind_birthday:

                # remind_birthday function defined in Birthday class, birthday.py file
                remind = Birthday.remind_birthday(phrase)
                
                # If birthday is not in the file let user know
                if remind == None:
                    print("Birthday isn't added")
                    say("birthday isn't added")
                    # Ask user if they wanna add it
                    x = input("Do you want to add it Y/N? ").lower()
                    if x == "yes" or x == 'y':
                        name = input("Name: ")
                        Birthday.add_birthday(name)
                    else:
                        listen()
                        pass

                if remind != None:
                    print(f"{remind['Name']} birthday is on {remind['Birthday']}")
                    say(f"{remind['Name']} birthday is on {remind['Birthday']}")
                continue

            # Holidays
            elif "when is" in phrase or "holidays list" in phrase:
                show_holiday(phrase)
                continue
            
            # Add some notes to a text file
            elif "add a note" in phrase:
                print("making a note...")
                say("making a note")
                notes = listen()
                with open('notes.txt', 'a') as file:
                    file.write(f"\n{notes}")
                print("Noted!")
                say("Noted!")
                continue
            
            # Show the notes in the text file
            elif "print the notes" in phrase or "show the notes" in phrase or "what are the notes" in phrase:
                with open('notes.txt', 'r') as file:
                    notes_reader = file.readlines()
                    if not notes_reader:
                        print("Nope! no notes at hand. Add some notes")
                        say("Nope! no notes at hand. Add some notes")
                    for i in notes_reader:
                        print(i, end="")
                    print("")
                print("")
                continue

            # Phone number

            # Add phone.no to contacts
            elif add_phone_number or "add phone number" in phrase or "add a contact" in phrase:

                # add_phone_number defined in PhoneNumber class, contacts.py file
                PhoneNumber.add_phone_number(phrase)
                print("Phone number added successfully!")
                say("Phone number added successfully!")
                continue
            
            # Show phone.no from contacts
            elif show_phone_number or "show a phone number" in phrase or "show a contact" in phrase:

                # show_phone_number defined in PhoneNumber class, contacts.py file
                try:
                    show_no = PhoneNumber.show_phone_number(phrase)
                    print(f"{show_no['Name']} is {show_no['Phone Number']}")
                    say("here's your number")
                except TypeError:
                    print("Did you mean 'a phone number or a contact?'")
                continue

            elif "show contacts" in phrase or "show all contacts" in phrase or "show my contacts" in phrase:
                with open('contacts.csv', 'r') as file:
                    contacts_list = csv.DictReader(file)
                    for i in contacts_list:
                        print(f'{i["Name"]} - {i["Phone Number"]}')
                continue


            # Google search
            elif "what" in phrase or "why" in phrase or "where" in phrase or "when" in phrase or "how" in phrase or "who" in phrase:
                print("Here are your results...")
                say("Here are your results")
                google_search(phrase)

            # Bye
            elif "bye" in phrase or "sayonara" in phrase:
                say("bye-bye, have a good day")
                exit()

            # If none of the above 
            # Make user repeat
            elif phrase != "none":
                print("I can't get what you mean. Could you please repeat that?\n")
                say("I can't get what you mean. Could you please repeat that")

    main()

except (KeyboardInterrupt, EOFError):
    pass
