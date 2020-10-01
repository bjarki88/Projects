

def intersection(first_1,second_2):
    set_1(first_1)
    set_2(second_2)
    intersec = [int(num) for num in first_1 if num in second_2]
    intersec_return = sets(intersec)
    return intersec_return

def union(one, two):
    mengi = set_1(one) + set_2(two)
    sammengi = sets(mengi)
    return sorted(sammengi)

def sets(first):
    first_list = []
    for num in first:
        if num not in first_list:
            first_list.append(num)
    first_list = [int(i) for i in first_list]
    return first_list

def set_1(sort_set):
    sorted_list_1 = sorted(sets(sort_set))
    return sorted_list_1

def set_2(sort_set):
    sorted_list_2 = sorted(sets(sort_set))
    return sorted_list_2



#Main program 
first_list = input('Enter elements of a list separated by space: ').strip().split()
second_list = input('Enter elements of a list separated by space: ').strip().split()

print('Set 1: ',set_1(first_list))
print('Set 2: ',set_2(second_list))
print('Union: ',union(first_list,second_list))
print('Intersection: ',intersection(first_list,second_list))