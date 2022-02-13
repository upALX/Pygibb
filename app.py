keyword_gibbet_value = "banana"
letters_acerted = ["-","-","-","-","-","-",]
kick_right_word = False
when_user_hanged = False

print('Hellow! Welcome to Pygibb :D')
print('You need play a game inserting one letter at a time!')

kick_gibbet_value = input('Please, insert a letter: ').upper()

verify_kick_value_numeric = kick_gibbet_value.isdigit()

while(verify_kick_value_numeric == True):
    try:
        print('Ooops... You need to insert a letter, not a number! ')
        kick_gibbet_value = input('Please, insert a letter: ').upper()
        verify_kick_value_numeric = kick_gibbet_value.isdigit()
    except ValueError:
        print('A value error is happen... Try use only one letter, never number!')
    continue
else:
    while(not kick_right_word and not when_user_hanged):

        position_letter = 0

        for letter_inside_keyword in keyword_gibbet_value:
            if(kick_gibbet_value == letter_inside_keyword.upper()):
                letters_acerted[position_letter] = letter_inside_keyword
            position_letter = position_letter + 1
        print(letters_acerted)

        kick_gibbet_value = input('Please, insert a letter: ').upper()
