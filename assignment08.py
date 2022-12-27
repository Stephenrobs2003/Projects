phoneFaves = {}
def addPhoneFave():
    # replace = False
    if len(phoneFaves) == 3:
        print("You'll have to remove a fave first")
        return

    key = input("Enter your name:")
    if len(key) > 30:
        print("You'll have to enter a shorter name")
        return

    if key in phoneFaves:
        print("This will replace the existing number for " + key)
        x = input("Do you want to continue? (y/n):")
        if x == "n":
            print("The number for " + key + " has not been replaced")
            return

    # replace = True
    y = input("Enter number:")
    phoneFaves[key] = y
    print(key + " has been added")
    return

def findPhoneFaveNumber():
    name = input("Enter Your Name")
    if name in phoneFaves:
        print(phoneFaves[name])
        # print(phoneFaves.get(name))
    else:
        print(name + " not found")

def removePhoneFave():
    name = input("Enter Your Name")
    if name in phoneFaves:
        del phoneFaves[name]
        # phoneFaves.pop(name)
        print(name + " is no longer a fave")
    else:
        print(name + " not found")

def findPhoneFaveName():
    number = input("Enter your number")
    # if number in phoneFaves.values():
    #     return print(phoneFaves.get(number))
    if number in phoneFaves.values():
        for i in phoneFaves.keys():
            if phoneFaves[i] == number:
              return print(i)
    else:
        return print(number + " not found")

def printPhoneFaves():
    if len(phoneFaves.values()) > 0:
        for name in sorted(phoneFaves):
            print(name + ((35 - (len(name))) * " ") + phoneFaves[name])
    else:
        return print("You have no faves")































