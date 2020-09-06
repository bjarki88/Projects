flalb = input('Input f|a|b (fibonacci, abundant or both): ')
if flalb == 'b':
    length = int(input('Input the length of the sequence: '))
    print('Fibonacci Sequence:')
    print('-----------------')
    
    first_number = 0 # start with 0 and 1 because the Fibonacci sequence always starts with 0 and 1
    second_number = 1
    print(first_number)
    print(second_number)

    for fibonacci in range(2,length):
        fibonacci = first_number + second_number
        first_number = second_number
        second_number = fibonacci
        print(fibonacci)

    max_number = int(input('Input the max number to check: '))
    print('Abundant numbers:')
    print('-----------------')

    sum_ = 0
    for abundant_numbers in range(1,max_number+1):
        for divisors in range(1, abundant_numbers):
            if (abundant_numbers % divisors == 0):
                sum_ = divisors + sum_
        if sum_ > abundant_numbers:
            print(abundant_numbers)
        sum_ = 0


elif flalb == 'a':
    max_num = int(input('Input the max number to check: '))
    print('Abundant numbers: ')
    print('-----------------')

    sum_ = 0
    for abundant_numbers in range(1,max_num+1):
        for divisors in range(1, abundant_numbers):
            if (abundant_numbers % divisors == 0):
                sum_ = divisors + sum_
        if sum_ > abundant_numbers:
            print(abundant_numbers)
        sum_ = 0

elif flalb == 'f':
    length = int(input('Input the length of the sequence: '))
    print('Fibonacci Sequence: ')
    print('-----------------')

    first_number = 0
    second_number = 1
    print(first_number)
    print(second_number)

    for fibonacci in range(2,length):
        fibonacci = first_number + second_number
        first_number = second_number
        second_number = fibonacci
        print(fibonacci)


