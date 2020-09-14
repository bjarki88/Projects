pass_word = input('Please enter a password:')

incorrect = 0
correct = 0

while pass_word != 'q': # Create a constant so that if the user presses q it ends the loop
    upper_case = False
    lower_case = False
    number = False
    if 6 < len(pass_word) or len(pass_word) < 20: # Create the range that the string must fall under
        for i in pass_word:
            if i.isupper():
                upper_case = True
            elif i.islower():
                lower_case = True
            elif i.isdigit():
                number = True

        if not lower_case:
            print('At least one lower case letter needed')
        if not upper_case:
            print('At least one upper case letter needed')
        if not number:
            print('At least one number needed')
        if number and lower_case and upper_case:
            correct = correct + 1
            print('Valid password of length', len(pass_word))
        else:
            incorrect = incorrect + 1
    else:
        print('Invalid length')
        incorrect = incorrect + 1
    pass_word = input('Enter a new password: ')

print('You tried {} passwords, {} correct, {} invalid'.format((correct + incorrect), correct, incorrect))