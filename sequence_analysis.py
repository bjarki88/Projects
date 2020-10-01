import string
decimal_point = 4

def open_file(file_name):
    file_content = []#Create an empty lists
    for lines in file_name:
        lines = lines.strip('\n')#Strip the whitespace and letters
        file_content.append(lines)#Put it in the file_content list
    return file_content

def sequence(file_content):
    file_con = open_file(file_content)
    new_content = []
    for num in file_con:
        try:#Use the try expect to filter out everything that is not a number
            num = float(num)
            num_rounded = round(num, decimal_point)#Round each number with 4 decimal points
            new_content.append(num_rounded)#Then puts the numbers in a new list
        except ValueError:
            pass
    return new_content


def cumulitive(file_cumsum):
    cumsum = sequence(file_cumsum)#Call the sequence function to get the list
    new_list=[]#Create a new list
    total = 0
    for num in range(0,len(cumsum)):# We need to know how many numbers are in the list
        total = total + float(cumsum[num])#Use total to create the Cumulative sum
        total = round(total, decimal_point)# Round to 4 decimal points
        new_list.append(total)#Then put the rounded number in the new_list list
    return new_list

def sorted_list(file_sort):
    sort_list = sorted(sequence(file_sort)) #Call the functin Sequence and sort it
    return sort_list

def median_list(file_median):
    try:
        median = sorted_list(file_median)#Call the sorted list
        if len(median) % 2 == 0:#Use len to see if we have even amount of numbers
            medium = (median[len(median) // 2] + median[(len(median) - 1) // 2]) / 2
            return round(medium, decimal_point)
        else:#Here we take the two numbers in the middle and divide them
            medium = median[len(median) // 2]
            return round(medium, decimal_point)
    except IndexError: #If we have odd amount of numbers just find the middle of the list
        return ''     #If there is nothing in the file we return noting instead of error

def process_all_files(file_read):
    print()
    try: #Use try/Except so that the program prints out if the file is not found
        for files in file_read:#use join to covert the list into a string
            sequence_list = ' '.join([str(num) for num in sequence(open(files,'r'))])
            cumsum_list = ' '.join([str(num) for num in cumulitive(open(files,'r'))])
            sort_list = ' '.join([str(num) for num in  sorted_list(open(files,'r'))])
            med_list = median_list(open(files,'r'))
            print('File', files)          #Use newline and tab to get a nice output
            print('\tSequence:\n\t\t{} '.format(sequence_list))          
            print('\tCumulative sum:\n\t\t{} '.format(cumsum_list))
            print('\tSorted sequence:\n\t\t{} '.format(sort_list))
            print('\tMedian:\n\t\t{}\n'.format(med_list))
    except FileNotFoundError:
        print('File {} not found'.format(''.join(files)))
        
# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)
