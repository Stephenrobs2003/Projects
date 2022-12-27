def isValidVariableName(name):
    length = len(name)
    if name[0].isalpha() == False and name[0] != "_":
        return False
    for i in range(length):
        if name[i].isalnum() == False and name[i] != "_":
            return False
    return True

def camelCase(text):
    length = len(text)
    for i in range(length):
        if text[i] == " ":
            text = text[:i +1] + text[i + 1].upper() + text[i + 2:]
    return text.replace(" ", "")


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

def findWordCrossIndex(horizontalWord,verticalWord):
    for i in range(len(horizontalWord)):
        for x in range(len(verticalWord)):
            if horizontalWord[i] == verticalWord[x]:
                return i
        if i == (len(horizontalWord)-1):
            return -1

def printWordCrossIndex(horizontalWord,verticalWord):
    for i in range(len(horizontalWord)):
        for x in range(len(verticalWord)):
            if horizontalWord[i] == verticalWord[x]:
                break
        if i == (len(horizontalWord)-1):
            print("No word cross")
            return








