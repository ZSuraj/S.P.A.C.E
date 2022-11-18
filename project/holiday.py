import holidays
from datetime import datetime
from functions import google_search, say

# Current datetime
year = datetime.now()
# Current year
year = int(year.strftime("%Y"))

# Using holidays module
# Passing the year variable to the years parameter
days = holidays.IN(years=year) + holidays.US(years=year)

def show_holiday(phrase):
    
    # Redirect to google search
    if len(phrase.split()) > 5:
        google_search(phrase)

    elif "holidays list" in phrase:
        say("here is your holidays list")
        for i in days:
            print(f"{i} - {days[i]}")

    else:

        try:
            
            # Getting the day
            phrase = phrase.replace("when is", "").lower().strip()
            # Looping through the (days) dictionary
            for i in days:
                day = days[i].lower()

                if phrase == "pongal" or phrase == "makar sankranti":
                    day = day.replace("makar sankranti / ", "").replace("/ pongal", "")

                # Date (output) for the user input 
                if phrase == day.strip():
                    i = i.strftime("%B %d, %Y")
                    print(f"{phrase.capitalize()} is on {i}")
                    say(f"{phrase} is on {i}")

        except UnboundLocalError:
            print("When is WHAT? say it again")
            say ("When is what? say it again")
