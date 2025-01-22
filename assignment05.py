# Function to check if a given name is a valid variable name
def isValidVariableName(name):
    length = len(name)
    # Check if the first character is a letter or underscore
    if name[0].isalpha() == False and name[0] != "_":
        return False
    # Check if all characters are alphanumeric or underscore
    for i in range(length):
        if name[i].isalnum() == False and name[i] != "_":
            return False
    return True

# Function to convert a string to camelCase
def camelCase(text):
    length = len(text)
    for i in range(length):
        if text[i] == " ":
            text = text[:i + 1] + text[i + 1].upper() + text[i + 2:]
    return text.replace(" ", "")

# Function to print a word block of a given length
def printWordBlock(word, length):
    if length < len(word):
        print(str(length) + " is less than the length of " + word)
    else:
        index_of_word = 0
        for row in range(length):
            row_text = ""
            for col in range(length):
                if index_of_word == len(word):
                    index_of_word = 0
                row_text = row_text + word[index_of_word]
                index_of_word = index_of_word + 1
            print(row_text)

# Function to find the index where two words cross
def findWordCrossIndex(horizontalWord, verticalWord):
    for i in range(len(horizontalWord)):
        for x in range(len(verticalWord)):
            if horizontalWord[i] == verticalWord[x]:
                return i
        if i == (len(horizontalWord) - 1):
            return -1

# Function to print the index where two words cross
def printWordCrossIndex(horizontalWord, verticalWord):
    for i in range(len(horizontalWord)):
        for x in range(len(verticalWord)):
            if horizontalWord[i] == verticalWord[x]:
                break
        if i == (len(horizontalWord) - 1):
            print("No word cross")
            return
