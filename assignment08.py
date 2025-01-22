# Dictionary to store favorite phone numbers
phoneFaves = {}

# Function to add a favorite phone number
def addPhoneFave():
    # Check if the maximum number of favorites is reached
    if len(phoneFaves) == 3:
        print("You'll have to remove a fave first")
        return

    key = input("Enter your name:")
    # Check if the name is too long
    if len(key) > 30:
        print("You'll have to enter a shorter name")
        return

    # Check if the name already exists in the favorites
    if key in phoneFaves:
        print("This will replace the existing number for " + key)
        x = input("Do you want to continue? (y/n):")
        if x == "n":
            print("The number for " + key + " has not been replaced")
            return

    # Add or replace the phone number
    y = input("Enter number:")
    phoneFaves[key] = y
    print(key + " has been added")
    return

# Function to find and print the phone number for a given name
def findPhoneFaveNumber():
    name = input("Enter Your Name")
    if name in phoneFaves:
        print(phoneFaves[name])
    else:
        print(name + " not found")

# Function to remove a favorite phone number
def removePhoneFave():
    name = input("Enter Your Name")
    if name in phoneFaves:
        del phoneFaves[name]
        print(name + " is no longer a fave")
    else:
        print(name + " not found")

# Function to find and print the name for a given phone number
def findPhoneFaveName():
    number = input("Enter your number")
    if number in phoneFaves.values():
        for i in phoneFaves.keys():
            if phoneFaves[i] == number:
                return print(i)
    else:
        return print(number + " not found")

# Function to print all favorite phone numbers
def printPhoneFaves():
    if len(phoneFaves.values()) > 0:
        for name in sorted(phoneFaves):
            print(name + ((35 - (len(name))) * " ") + phoneFaves[name])
    else:
        return print("You have no faves")
