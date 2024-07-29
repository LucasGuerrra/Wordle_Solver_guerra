import os
import time

clear = lambda: os.system('cls')

#The letters that are present,the ones that are not and the words that the user said it can't be, respectively
exists = []
no_exists = []
removal = []

def Search_Word (letter,exists, no_exists,removal):
    #working out how to find the desired file
    path = 'letters/' + letter + '.txt'
    file = open(path, 'r')
    
    return_word = ''
    previous_pontuation = 0

    #this will go through each line(each word) in the file
    for line in file:
        #these will remove spaces and \n from the strings, be a variable in case the letter in the word is in the "no_exists" list,
        #be a list that can be reseted for each word so that we dont lose the "exists" file's information(i just discovered that if u use
        #'variable' = 'list', that links both lists, and instead i need to use the '.copy' so they dont link. LOL), a way of tracking which words
        #are have the most letters matching with the "exists" list and a variable that will end the search if it founds a perfect match, all respectively
        word = line.strip()
        fuck_off = False
        pontuation = 0

        for big_no in removal:
            if word == big_no:
                fuck_off = True
                break
        if fuck_off == True:
            continue

        for character in word:
            #goes through each letter in the non existant letters' list
            for not_letter in no_exists:
                #checking if both letter match
                if not_letter == character:
                    #If they match, than activate a variable so that it can escape the for loops
                    fuck_off = True
                    pontuation = 0
                    break
            if fuck_off == True:
                break
        if fuck_off == True:
            break

            # for yes_letter in range(len(digital_exists)):
            #     if digital_exists[yes_letter] == character:
            #         pontuation += 1
            #         digital_exists[yes_letter] = ''
            #         break
        for i in range(5):
            if exists[i] == '':
                continue
            if list(word)[i] == exists[i]:
                print(exists[i])
                pontuation += 1

        if pontuation > previous_pontuation:
            print(pontuation, return_word, word)
            return_word = word
            previous_pontuation = pontuation

            if pontuation == 5:
                break
    
    if return_word == '':
        return_word = "Could'n find a possible match"
        
    file.close()
    return return_word
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
escape = False

while True:
    clear()
    letters = input("Type the next letter that exists(if it's unknown type '-'): ")
    for i in range(4):
        exists.append(letters)
        clear()
        print(exists)
        letters = input("Type the next letter that exists(if it's unknown type '-'): ")
    clear()
    exists.append(letters)
    print(exists)

    time.sleep(3)
    clear()

    letters = input("Type all the letters know not to be (don't put spaces between them): ")
    no_exists += list(letters)
    print(no_exists)

    time.sleep(3)
    clear()

    print(exists)
    print(no_exists)
    if exists[0] == '':
        letter = input("Type a letter you want to search words for: ")
    else:
        letter = exists[0]
        print("Searching for the letter '",letter,"'")

    time.sleep(2.5)
    clear()

    while True:
        awnser = Search_Word(letter,exists, no_exists,removal)
        print(awnser, ', is the best match we could find for now')
        check = input('Does this word work?(Y/N): ')
        if check != 'N':
            escape = True
            break
        else:
            removal.append(awnser)
            break

    if escape == True:
        break