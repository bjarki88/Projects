flalb = input('Input f|a|b (fibonacci, abundant or both): ')
if flalb == 'a':
    max_num = int(input('Input the max number to check: '))

    sum_ = 0
    for abundant_num in range(1,max_num+1):
        for divisors in range(1, abundant_num):
            if (abundant_num % divisors == 0):
                sum_ = divisors + sum_
        if sum_ > abundant_num:
            print(abundant_num)
        sum_ = 0