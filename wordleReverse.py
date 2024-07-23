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
while True:
    while True:
        letter = input("Type a letter know(end it type 'Ç'): ")
        if letter == 'Ç':
            break
        else:
            exists.append(letter)
    print(exists)
    while True:
        letter = input("Type a letter know to be not(don't repeat them, and to end it type 'Ç'): ")
        if letter == 'Ç':
            break
        else:
            no_exists.append(letter)
    print(no_exists)

    letter = input("Type a letter you want to search words for: ")



    while True:
        awnser = Search_Word(letter,exists, no_exists,removal)
        print(awnser, ', this is the best match we could find for now')
        check = input('Does this word work?(Y/N): ')
        if check != 'N':
            escape = True
            break
        else:
            removal.append(awnser)
            break

    if escape == True:
        break