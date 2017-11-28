def handle_string(value):
    letters = 0
    digits = 0
    for element in value:
        if element.isdigit():
            digits += 1
        elif element.isalpha():
            letters += 1
    return 'Letters - {}\nDigits - {}\n'.format(letters,digits)



