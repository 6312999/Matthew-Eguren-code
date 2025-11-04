# Function 1: 
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):   #calling the function
   return list(set(numbers))              #allows me to make the list of numbers
numbers=[3,3,2,4,2,5,1,3,8,3]              #giving the list of numbers
print(remove_duplicates_and_sort(numbers)) #calling back the function


# Function 2: 
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):       #calling the function
   result= [ ]            #this makes an empty list to put values
   total= 0                  #starts the total at 0
   for num in arr: #make it go through every number in the array
       total+=num           #adds each number to the total
       result.append(total)  #adds total to the result list
   return result       #returns the new list
print(cumulative_sum([1,2,3,4,5]))   #call back the function


# Function 3: 
# This function takes a list and a step value (N), and returns every Nth element from the list.
def slice_every_nth(lst, step):     #calling the function
   if step <= 0:                  #if step is 0 or negative
       return []               #return an empty list (not valid)
   return lst[step-1::step] #starts at (step-1) so 2 and goes up in increments of 3(step), until 9
print(slice_every_nth([1,2,3,4,5,6,7,8,9], 3)) #call back function


# Function 4: 
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2): #calling the function
   if len(list1) != len(list2): #checks if both lists are the same length
       return 0 #if not, return 0 (invalid for dot product)
   product = sum(x * y for x, y in zip(list1, list2)) # multiplies matching elements and adds them together
   # zip(list1, list2) pairs each number from both lists, so 1*4,2*5,3*6
   return product                    # returns the final dot product value
print(dot_product([1,2,3], [4,5,6]))  # call back the function


#Function 5:
matW = [[1,2],          #Multiplies by column, 1x5+2x7, then 1x6+2x8
    [3,4]]              #Multiplies by row 3x5+4x7 then 3x6+4x8

matZ = [[5,6],         #Multiplies by column, 1x5+2x7, then 1x6+2x8
    [7,8]]          #Multiplies by row 3x5+4x7 then 3x6+4x8

result = [[0,0],        #show how i want the answers to be provided
    [0,0]]

for i in range(len(matW)):          #define the len of i
    for j in range(len(matZ[0])):  #define the len of j
       for k in range(len(matW)):   #define the len of k
           result[i][j] += matW[i][k] * matZ[k][j]  #how the math will be calculated

print(result) # Print the result