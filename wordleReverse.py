import os

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
        end = False

        #will go through each letter in the 'striped' word from the file  for both the checking if the letter doesn't exists or it does, respectively
        for character in word:
            #goes through each letter in the non existant letters' list
            for not_letter in no_exists:
                #checking if both letter match
                if not_letter == character:
                    print (not_letter,word)
                    #If they match, than activate a variable so that it can escape the for loops
                    fuck_off = True
                    break
            if fuck_off == True:
                break

            for yes_letter in range(len(digital_exists)):
                if digital_exists[yes_letter] == character:
                    pontuation += 1 
                    digital_exists[yes_letter] = ''
                    break

            if pontuation > previous_pontuation:
                for big_no in removal:
                    if word == big_no:
                        fuck_off = True
                        break
                if fuck_off == True:
                    break

                print(pontuation, return_word, word)
                return_word = word
                previous_pontuation = pontuation

                if pontuation == 5:
                    end = True
                    break

                fuck_off = True
                break
        
        #I like this part cause i fucked up a lot, cause i didnt realise that if the "fuck_off" was activated i can't just break the loop,
        #i insisted a lot in this mistake until i realized that i should have used the continue so that the code just jumps to the next word

        #basicaly if it escaped the for loop above, either they came from the a word that had a letter that didn't exists (should only go to 
        #the next word), or they only had matching letters with the 'exists' list (should break the entirety of the loops and awnser that) or
        #they didn't match all the letters but also didn't have anything to give conflict with the "no_exsits" list (should print a sorry message)
        if end == True:
            print('end')
            break
        if fuck_off == True:
            continue
    
    if return_word == '':
        return_word = "Could'n find a possible match"
        
    file.close()
    return return_word
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
escape = False
while True:
    while True:
        letter = input("Type a letter know(don't repeat them, and to end it type 'esc'): ")
        if letter == 'esc':
            break
        else:
            exists.append(letter)
    print(exists)
    while True:
        letter = input("Type a letter know to be not(don't repeat them, and to end it type 'esc'): ")
        if letter == 'esc':
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