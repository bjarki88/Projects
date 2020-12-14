def print_counted_votes(b_dict):
    for key, val in sorted(a_dict.items()):
        my_sum = sum(val)
        a_dict[key] = my_sum
        print('{}: {}'.format(key,my_sum))
    

def print_total_votes(a_dict):
    value_list = list(a_dict.values())
    the_sum = sum(value_list)
    print('Total no. of votes: {}'.format(the_sum))

def make_dict(name, vote):
    try:
        vote = int(vote)
        vote_list.append(vote)
        if name in a_dict.keys():
            a_dict[name] += vote_list
        else:
            a_dict[name] = vote_list
        return a_dict
    except ValueError:
        print('Invalid no. of votes!')
        return a_dict


# Main program  
a_dict = {}
vote = True
try:
    while vote != []:
        vote_list = []
        name, vote = input('Candidate and votes: ').lower().split()
        a_dict = make_dict(name, vote)
except ValueError:
    pass

print(a_dict)
print_counted_votes(a_dict)
print_total_votes(a_dict)