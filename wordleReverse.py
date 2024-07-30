import os
import time

clear = lambda: os.system('cls')

def Search_Word (letter, no_exists,removal):
    #working out how to find the desired file
    path = 'letters/' + letter + '.txt'
    file = open(path, 'r')
    
    return_word = ''
    previous_pontuation_primal = 0
    previous_pontuation_side = 0

    #this will go through each line(each word) in the file
    for line in file:
        #these will remove spaces and \n from the strings, be a variable in case the letter in the word is in the "no_exists" list,
        #be a list that can be reseted for each word so that we dont lose the "exists" file's information(i just discovered that if u use
        #'variable' = 'list', that links both lists, and instead i need to use the '.copy' so they dont link. LOL), a way of tracking which words
        #are have the most letters matching with the "exists" list and a variable that will end the search if it founds a perfect match, all respectively
        word = line.strip()
        digital_exists = exists.copy()
        fuck_off = False
        pontuation_primal = 0
        pontuation_side = 0

        for big_no in removal:
            if word == big_no:
                fuck_off = True
                break
        if fuck_off == True:
            continue

        for i in range(5):
            
            #goes through each letter in the non existant letters' list
            for not_letter in no_exists:
                #checking if both letter match
                if not_letter == word[i]:
                    #If they match, than activate a variable so that it can escape the for loops
                    fuck_off = True
                    pontuation_primal = 0
                    pontuation_side = 0
                    break
            if fuck_off == True:
                break

            for yes_letter in range(len(digital_exists)):
                if digital_exists[yes_letter] == word[i]:
                    pontuation_side += 1 
                    digital_exists[yes_letter] = ''
                    break

            if positioned[i] == '':
                continue
            if list(word)[i] == positioned[i]:
                pontuation_primal += 1
            else:
                pontuation_primal = 0
                pontuation_side = 0
                break
        for letter in digital_exists:
            if letter != '':
                pontuation_primal = 0
                pontuation_side = 0
                break

        if pontuation_primal > previous_pontuation_primal:
            return_word = word
            previous_pontuation_primal = pontuation_primal
            previous_pontuation_side = pontuation_side

            if pontuation_primal == 5:
                break
        elif pontuation_primal == previous_pontuation_primal:
            if pontuation_side > previous_pontuation_side:
                return_word = word
                previous_pontuation_primal = pontuation_primal
                previous_pontuation_side = pontuation_side
    
    if return_word == '':
        return_word = "Could'n find a possible match"
        
    file.close()
    return return_word
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    escape = False

    #The letters that are present,the ones that are not and the words that the user said it can't be, respectively
    positioned = []
    exists = []
    no_exists = []
    removal = []

    while True:
        positioned = []
        clear()
        letters = input("Type the next letter that is positioned(if it's unknown just press ENTER): ")
        for i in range(4):
            positioned.append(letters)
            clear()
            print(positioned)
            letters = input("Type the next letter that positioned(if it's unknown just press ENTER): ")
        clear()
        positioned.append(letters)
        print(positioned)

        time.sleep(2)
        clear()

        letters = input("Type all the letters know to exist(don't put spaces between them): ")
        exists = list(letters)
        print(exists)

        time.sleep(2)
        clear()

        print(no_exists)
        letters = input("Type all the letters know not to be(don't put spaces between them): ")
        no_exists += list(letters)
        print(no_exists)

        time.sleep(2)
        clear()

        print(no_exists)
        if positioned[0] == '':
            letter = input("Type a letter you want to search words for: ")
        else:
            letter = positioned[0]
            print("Searching for the letter '",letter,"'")

        time.sleep(1.5)
        clear()

        while True:
            awnser = Search_Word(letter, no_exists,removal)
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