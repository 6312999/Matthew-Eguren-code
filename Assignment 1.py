# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    list = [num1, num2, num3]   #giving the list
    return (max(list)) #telling it to give me the maximum
num1 = int(input("Enter a number: "))   #letting user chose value
num2 = int(input("Enter a number: "))   #letting user chose value
num3 = int(input("Enter a number: "))   #letting user chose value
print({built_in_functions_max(num1, num2, num3)}) 

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    list = [num1, num2, num3] #giving the list
    return (min (list)) #telling it to give me the minimum
num1 = int(input("Enter a number: ")) #letting user chose value
num2 = int(input("Enter a number: ")) #letting user chose value
num3 = int(input("Enter a number: ")) #letting user chose value
print({built_in_functions_min(num1, num2, num3)}) #recall function and tell the code to print out my result

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:             #when you input a value above 0, returns positive
        return("Positive")
    elif number < 0:           #when you input a value below 0, returns negative
        return ("Negative")
    else:                      #anything else (so only the number 0), will give you 0
        return ("Zero")
number = int(input("Enter a number: "))    #let user chose values
print ({check_number(number)})       #recalling the function to get my result


# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    for i in range (1, rows +1 ):#the range is from 1 to value inputted (without the +1 it's row inputted -1)
        print ('*' * i)
rows= int(input("Enter a number of rows: "))        #let user input their value
{star_shape(rows)}      #recalling the function to get my result

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    count = 1       #counts the numbers, so 1 starts at 1 and increases in increments of 1
    while count <= limit:   #continues the addition until you hit the limit (inputted value)
        if count % 3 == 0:  #if % 3 gives no remainder the print multiple of 3
            print ("Multiple of 3")
        else:                #anything that doesn give 0 as a remainder is not going to return Multiple of 3, it'll give 
            print(count)    
        count += 1                     #number increases by a value of 1
limit = int(input("Enter the limit:"))      #let user put in the values
count_multiples_of_3(limit)                 #recall function

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):        #define variable
    total= 0                                  
    for num in range (start, end+1):    # the "end" gives you the value inputted -1, the plus 1 makes it end where you actually tell it to 
            if num % 2 == 0:        #  % 2 ==0 means to give me all the values that equal to 0 when being divided by 2     
                total += num        #  Total is equal to the total (0) plus the value you enter
    return total
start = int(input("Enter a number for the start: "))   #let user put in the values 
end = int(input("Enter a number for the end: "))       #let user put in the values
print (f"The sum of even numbers in a given range is: {sum_of_even_numbers(start, end)}")   #recalling function and printing out statement
end = int(input("Enter a number for the end: "))
print (f"The sum of even numbers in a given range is: {sum_of_even_numbers(start, end)}")

