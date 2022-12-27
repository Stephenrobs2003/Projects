import random
def green_letter(letter):
    return '\033[92m' + letter + '\033[0m'


def yellow_letter(letter):
    return '\033[93m' + letter + '\033[0m'


def generate_word_list():
    word_list = []
    my_file = open("words.txt","r")
    for line in my_file:
        word = line.strip(" ")
        word_list.append(word)
        # word_list.append(line.strip(" "))
    my_file.close()
    return word_list

def get_guess(word_list):
    done = False
    while done == False:
        guess = input("Enter a guess: ")
        if guess in word_list:
            return guess

def pick_word(word_list):
    string = random.randint(0, len(word_list))
    return (word_list[string])

    # if len(word_list) > 0:
    #     words = random.choice(word_list)
    #     if words != "None":
    #         print(words)

    # my_file = open("words.txt","r")
    # word_list = my_file.readlines()
    # words = random.choice(word_list)
    # my_file.close()
    # print(words)

def is_game_over(word, guesses):
    if len(guesses) == 6 or word in guesses:
        return True
    else:
        return False

def display_board(word, guesses):
    print("+-----+")
    length_of_guesses = 0
    for words in guesses:
        string = ""
        for i in range(len(word)):
            character = words[i]
            if word[i] == words[i]:
                character = green_letter(words[i])
            elif words[i] in word:
                character = yellow_letter(words[i])
            string = string + character
        length_of_guesses = length_of_guesses + 1
        print("|" + string + "|")

    length_of_guesses = 6 - length_of_guesses
    for i in range(length_of_guesses):
        print("|" + "     " + "|")
    print("+-----+")
