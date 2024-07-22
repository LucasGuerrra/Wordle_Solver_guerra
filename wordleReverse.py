import os

#The letters that are present and the ones that are not, respectively
exists = ['R','E','B','A','Z']
no_exists = ['C','D','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y']
#letter to search in the files
letter = 'z'

def Search_Word (letter,exists, no_exists):
    #working out how to find the desired file
    path = 'letters/' + letter + '.txt'
    file = open(path, 'r')
    
    return_word = ''

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
                    #If they match, than activate a variable so that it can escape the for loops
                    fuck_off = True
                    break
            if fuck_off == True:
                break

            for yes_letter in digital_exists:
                if yes_letter == character:
                    pontuation += 1
                    digital_exists.remove(yes_letter)
            
            if pontuation == 5:
                return_word = word
                end = True
                break
        
        #I like this part cause i fucked up a lot, cause i didnt realise that if the "fuck_off" was activated i can't just break the loop,
        #i insisted a lot in this mistake until i realized that i should have used the continue so that the code just jumps to the next word

        #basicaly if it escaped the for loop above, either they came from the a word that had a letter that didn't exists (should only go to 
        #the next word), or they only had matching letters with the 'exists' list (should break the entirety of the loops and awnser that) or
        #they didn't match all the letters but also didn't have anything to give conflict with the "no_exsits" list (should print a sorry message)
        if end == True:
            break
        if fuck_off == True:
            continue
    
    if return_word == '':
        return_word = "Could'n find a possible match"
        
    file.close()
    return return_word

print(Search_Word(letter,exists, no_exists))