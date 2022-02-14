print('Welcome to the Pygibb!')

gybbed_user = False
right_kick_word = False
errors = 0
secret_word = 'league'.upper()
right_letters = ["_" for letter in secret_word]

print(right_letters)

while(not gybbed_user and not right_kick_word):
    kick_user = input('Hi, please insert a word: ').upper().strip()

    if(kick_user in secret_word):
        position_letter = 0
        for letter in secret_word:
            if(kick_user == letter):
                right_letters[position_letter] = letter
            position_letter += 1
        else:
            errors += 1

        gybbed_user = errors == 10
        right_kick_word = "_" not in right_letters
        print(right_letters)

if(right_kick_word):
    print('Você acertou!')
else:
    print('Você perdeu!')
