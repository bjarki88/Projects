flalb = input('Input f|a|b (fibonacci, abundant or both): ')
if flalb == 'b':
    length = int(input('Input the length of the sequence: '))
    print('Fibonacci Sequence: ')
    
    a = 0
    b = 1
    print(a)
    print(b)
    for fibonacci in range(2,length):
        fibonacci = a + b
        a = b
        b = fibonacci
        print(fibonacci)

    max_num = int(input('Input the max number to check: '))
    print('Abundant numbers:')

    sum_ = 0
    for abundant_num in range(1,max_num+1):
        for divisors in range(1, abundant_num):
            if (abundant_num % divisors == 0):
                sum_ = divisors + sum_
        if sum_ > abundant_num:
            print(abundant_num)
        sum_ = 0


elif flalb == 'a':
    max_num = int(input('Input the max number to check: '))
    print('Abundant numbers: ')

    sum_ = 0
    for abundant_num in range(1,max_num+1):
        for divisors in range(1, abundant_num):
            if (abundant_num % divisors == 0):
                sum_ = divisors + sum_
        if sum_ > abundant_num:
            print(abundant_num)
        sum_ = 0

elif flalb == 'f':
    length = int(input('Input the length of the sequence: '))
    print('Fibonacci Sequence: ')

    a = 0
    b = 1
    print(a)
    print(b)
    for fibonacci in range(2,length):
        fibonacci = a + b
        a = b
        b = fibonacci
        print(fibonacci)


