print('Hellow! Welcome to Pygibb :D')
print('You need play a game inserting one letter at a time!')

keyword_gibbet_value = []

kick_gibbet_value = input('Please, insert a letter: ')

kick_gibbet_value.upper().strip()
verify_kick_value_numeric = kick_gibbet_value.isdigit()


while(verify_kick_value_numeric == True):
    try:
        print('Ooops... You need to insert a letter, not a number! ')
        kick_gibbet_value = input('Please, insert a letter: ')
        verify_kick_value_numeric = kick_gibbet_value.isdigit()
    except ValueError:
        print('A value error is happen... Try use only one letter, never number!')
    continue

print('Verified!')
