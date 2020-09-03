n = int(input("Enter the length of the sequence: ")) # Do not change this line
for i in range(1, n+1):
    if i==1:
        length = fyrsta = i
    elif i == 2:
        length = seinna = i
    elif i == 3:
        length = þriðja = i
    else:
        length = fyrsta + seinna + þriðja
        fyrsta,seinna,þriðja = seinna,þriðja,length
    print(length)