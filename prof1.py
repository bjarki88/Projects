#secs = int(input("Input seconds: ")) # do not change this line
#hours = secs//(60*60) 
#secs_remain = secs % 3600
#minutes = secs_remain // 60
#secs_remain2 = secs % 60
#seconds = secs_remain2 
#print(hours,":",minutes,":",seconds) # do not change this line

max_int = 0

num_int = int(input("Input a number: "))    # Do not change this line
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line



