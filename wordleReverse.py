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
        digital_exists = exists.copy()
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

            for yes_letter in range(len(digital_exists)):
                if digital_exists[yes_letter] == character:
                    pontuation += 1 
                    digital_exists[yes_letter] = ''
                    break

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
print("ATENTION! If you ever want to erase something from one of the lists after it has already been sent, type 'Ç' when it asks you which letter to search for")
while True:
    letters = input("Type all the letters know: ")
    exists += list(letters)
    print(exists)

    letters = input("Type all the letters know not to be: ")
    no_exists += list(letters)
    print(no_exists)

    letter = input("Type a letter you want to search words for: ")
    while letter == 'Ç':
        print('Known letters: ', exists)
        removing = input('Type all the letters that should be removed from the known letters list: ')
        for letter in list(removing):
            exists.remove(letter)
        print('Known letters: ', exists)
        print('Known to not be letters: ', no_exists)
        removing = input('Type all the letters that should be removed from the known to not be letters list: ')
        for letter in list(removing):
            no_exists.remove(letter)
        print('Known to not be letters: ', no_exists)
        letter = input("Type a letter you want to search words for: ")

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