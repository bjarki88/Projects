def open_file(file_name): # Do not change this line
    '''Opens the given filename and returns its file object, or None if not found'''
    try:
        file_data = open(file_name, 'r')
        return file_data
    except FileNotFoundError:
        return None
    
def read_matrix(file_object): # Do not change this line
    '''Creates an n-by-n integer matrix by reading data from file_object. 
    The matrix is a list of lists.'''
    matrix = []
    for line in file_object:
        matrix.append([ int(num) for num in line.split()])
    return matrix

def row_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    row_sum = []
    for row in matrix:
        row = sum(row)
        row_sum.append(row)
    for row in row_sum:
        row_count = row
        if row_count == row:
            return row_sum
        else:
            return 0

def col_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    
    sum_list = [sum(x) for x in zip(*matrix)]
    return sum_list



def main(): # Do not change this line
    filename = 'final_exam.txt' #input('File name: ')
    file_stream = open_file(filename)
    matrix = read_matrix(file_stream)
    sum_row = row_sum_same(matrix)
    print(sum_row)
    sum_col = col_sum_same(matrix)
    print(sum_col)
    if sum_col == sum_row:
        print('Same sums')
    else:
        print('Not same sums')

# Main program starts here. Do not change it.
if __name__ == "__main__":
    main()