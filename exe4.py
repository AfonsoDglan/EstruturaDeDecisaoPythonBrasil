vowel = ['a','e','i','o','u'];
letter = str(input('Enter one letter: '));
if letter.lower() not in vowel:
    print('The letter entered is a consonant.');
elif letter.lower() in vowel:
    print('the letter entered is a vowel.');
else:print('ERROR.');