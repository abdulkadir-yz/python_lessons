alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
phone_book = {}

#Step 2: Create a phone book with letters as keys and empty dictionaries as values

for letter in alphabet:
    phone_book[letter.upper()] = {}   # Creating a phone book with letters as keys and empty dictionaries as values
print(phone_book)                     # Showing the phone book after creating it 

#Step 3: Show the keys and values of the phone book

print(phone_book.keys())              # Showing the keys of the phone book
print(phone_book.values())            # Showing the values of the phone book

#Step 4: Add a contact to the phone book
phone_book["A"]["Alice"] = "123-456-7890"   # Adding a contact to the phone book
phone_book["A"]["Bob"] = "987-654-3210"     # Adding another contact to the phone book
phone_book["A"]["Charlie"] = "555-555-5555" # Adding another contact to the phone book
print(phone_book["A"])                           # Showing the A contact in the phone book after adding it

#Step 5:
print(phone_book["A"].keys())              # Showing the keys of the A contact in the phone book
print(phone_book["A"].values())            # Showing the values of the A contact in the phone book
print(phone_book["A"])                     # Showing the A contact in the phone book

# --------------------------------------------------------
#way 2:
print(phone_book["A"].keys())              # Showing the keys of the A contact in the phone book
for name in phone_book["A"].keys():        # Looping through the keys of the A contact in the phone book
    print(name)                            # Showing the name of the contact in the phone book
for number in phone_book["A"].values():    # Looping through the values of the A contact in the phone book
    print(number)                          # Showing the number of the contact in the phone book

#Step 6: Add more contacts to the phone book
phone_book["C"]["Cally"] = "333-456-7890"  # Adding C contact to the phone book
phone_book["C"]["Casper"] = "222-456-7908" # Adding another C contact to the phone book
phone_book["C"]["Clint"] = "122-556-7908"  # Adding another C contact to the phone book
print(phone_book["C"].keys())              # Showing the keys of the C contact in the phone book 
print(phone_book["C"].values())            # Showing the values of the C contact in the phone book

phone_book["M"]["Mike"] = "123-444-7890"   # Adding M contact to the phone book
phone_book["M"]["Mary"] = "132-666-7908"   # Adding another M contact to the phone book
phone_book["M"]["Monica"] = "113-555-7908" # Adding another M contact to the phone book
print(phone_book["M"].keys())              # Showing the keys of the M contact in the phone book
print(phone_book["M"].values())            # Showing the values of the M contact in the phone book

phone_book["P"]["Paul"] = "123-456-7790"   # Adding P contact to the phone book
phone_book["P"]["Paulette"] = "132-456-8808" # Adding another P contact to the phone book
phone_book["P"]["Pete"] = "113-556-5508"   # Adding another P contact to the phone book
print(phone_book["P"].keys())              # Showing the keys of the P contact in the phone book
print(phone_book["P"].values())            # Showing the values of the P contact in the phone book

#Step 7: Show the entire phone book
print(phone_book.keys())
print(phone_book.values())

# BONUS :

name = "Mike"
phone = "123-444-7890"

name = name[0].upper() # Converting the name to uppercase
if name in phone_book.keys(): # Checking if the name is in the phone book
    print(f"{name} is already in the phone book.")
else:
    print(f"{name} is not in the phone book.") 

# BONUS 2:

phone = "123-444-7890"

found = False # First we need to create a variable to check if the phone number is found in the phone book or not

for letter , contacts in phone_book.items(): # Looping through the phone book
   for contact_name , contact_phone in contacts.items(): # Looping through the contacts in the phone book
       if contact_phone == phone: # Checking if the phone number is in the phone book
           print(f"{phone} is the phone number of {contact_name} in the phone book.") # If the phone number is found in the phone book, we print the name of the contact
           found = True
           break
   if found: 
       break    
if not found:
    print(f"The phone number {phone} is not in the phone book.")

# Bonus 3:

