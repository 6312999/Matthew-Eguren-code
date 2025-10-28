
def rotate_the_array(array_size, starting_integer):
    the_array = [0] * array_size
    for i in range(array_size -1, -1,-1): #range (start,end,step) so 6-1 (starts at 5), ends at -1 (not including -1), step
      the_array[i] = starting_integer
      starting_integer +=3

    print("Original array: ", the_array)
    print(the_array[5])   
    for i in range(0, array_size - 2, 2):
      temp = the_array[i]
      the_array[i] = the_array[i - 2]
      the_array[i + 2] = temp
   
   # Testing
    print("Rotated array: ", the_array)
    return the_array
rotate_the_array(6, 2)