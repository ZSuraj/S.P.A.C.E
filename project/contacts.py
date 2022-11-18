import csv

class PhoneNumber:
    def __init__(self) -> None:
        pass

    def add_phone_number(name):
        name = name.replace("add", "").replace("phone number", "").replace("a contact", "").strip()
        
        # Prompt the user for name if no name is provided
        if not name:
            name = input("Name: ")

        # Ask user to input phone.no
        number = input("Phone.no: ")
        
        # Add the details to the csv file
        with open('contacts.csv', 'a', newline="") as file:
            f = ["Name", "Phone Number"]
            bday_writer = csv.DictWriter(file, f)
            bday_writer.writerow({"Name" : name, "Phone Number" : number})
    
    def show_phone_number(name):
        name = name.replace("show", "").replace("a phone number", "").replace("a contact", "").strip()
        
        # Prompt the user for name
        if not name:
            name = input("Name: ")
        
        # Read the file
        with open('contacts.csv', 'r') as file:
            phone_number_reader = csv.DictReader(file)
            for i in phone_number_reader:
                if i["Name"] == name:
                    return i
