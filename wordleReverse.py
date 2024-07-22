import os

def Search_Word (letter):
    path = 'letters/' + letter + '.txt'
    file = open(path, 'r')

    #CRANE and SAUCY starting words
    exists = ['Z','E','B','R','A']
    no_exists = ['C','D','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y']
    return_word = ''

    for line in file:
        word = line.strip()
        fuck_off = False
        digital_exists = exists.copy()
        pontuation = 0
        end = False

        for character in word:
            for not_letter in no_exists:
                if not_letter == character:
                    fuck_off = True
                    print(word, ' fuck off')
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
        
        if end == True:
            break
        if fuck_off == True:
            continue
        
    file.close()
    return return_word
    
# letter = input('What letter do you want to search?: ')
print(Search_Word('z'))