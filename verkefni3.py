flalb = int(input('Input f|a|b (fibonacci, abundant or both): '))

start = 12
if flalb < start:
    print('Write a number above 12')
for i in range(start,flalb+1):
    if i % 2 == 0:
        print(i)