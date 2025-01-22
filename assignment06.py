import random

# Function to clean the plaintext by removing spaces, converting to lowercase, and padding with random letters if necessary
def cleanPlaintext(plaintext, key):
    plaintext1 = plaintext.replace(" ", "")
    plaintext1 = plaintext1.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if len(plaintext1) % len(key) == 0:
        return plaintext1
    else:
        number = len(plaintext1) % len(key)
        reminder = len(key) - number
        for i in range(reminder):
            random_letter = random.choice(alphabet)
            plaintext1 = plaintext1 + random_letter
    return plaintext1

# Function to determine the column order based on the key
def columnOrder(key):
    if len(key) >= 10:
        return "error"
    else:
        unique_letters = set(key)
        sorted_unique_letters = sorted(unique_letters)
        column_number = 1
        for ch in sorted_unique_letters:
            key = key.replace(ch, str(column_number))
            column_number = column_number + 1
        return key

# Function to print the columnar cipher table
def printColumnarCipher(columnOrder, plaintext):
    text = columnOrder + plaintext
    for i in range(len(text)):
        print(text[i], end='')
        if 0 == (i + 1) % 6 and i != 0:
            print("\n", end='')

# Function to get the text of a specific column in the plaintext
def getColumnText(plaintext, key, columnIndex):
    text = ""
    for i in range(columnIndex, len(plaintext), len(key)):
        text = text + plaintext[i]
    return text

# Function to encode the plaintext using the columnar cipher method
def columnarCipherEncode(printTable):
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    if len(key) > 10:
        print("error")
        return
    text = cleanPlaintext(plaintext, key)
    variable = columnOrder(key)
    if printTable:
        printColumnarCipher(variable, text)
    if len(key) == 1:
        getColumnText(text, key, 0)
    start_index = 1
    line = ""
    for i in range(len(text)):
        if start_index > len(key):
            start_index = 0
        line = line + getColumnText(text, key, start_index)
        start_index = start_index + 2
    print(line)
    return
