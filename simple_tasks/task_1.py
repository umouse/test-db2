def handle_number(number1,number2,number3):
    numbers = 0
    for number in range(number1, number2+1):
        if number % number3 == 0:
            numbers += 1
    return numbers


