import math #Importing math for square root

#Calculating the average of all the items in the list
def calculate_Avg(my_integer_list):
    #Initializing the list total variable as zero
    my_list_total = 0
    #Iterating each item im the list and adding those values in the list total variable
    for my_integer in my_integer_list:
        my_list_total = my_list_total + my_integer
        #print(f'my list total: {my_list_total}')
    
    
    print(f'list total is: {my_list_total}. total items in the list: {len(my_integer_list)}')
    print(f'average is: {my_list_total/len(my_integer_list)}')
    #Returning the average of all the items in the list
    return my_list_total/len(my_integer_list)
#function called sumSqDiff() that also accepts a list as an argument and returns the sum square of the difference of 
# list values and the average. sumSqDiff() implements this formula ssd= ∑_(i=0)^(N-1)▒〖(xi-x ̅)〗 where xi is the item
#  in the list at index i, and x ̅ is the average of all items.
def calculate_sumSqDiff(my_integer_list, my_list_average):
    #Initializing the my_sumSqDiff_list_total variable to 0
    my_sumSqDiff_list_total = 0
    #Iterating through each item of the list to implement the formula ssd= ∑_(i=0)^(N-1)▒〖(xi-x ̅)〗 where xi is the item
#  in the list at index i, and x ̅ is the average of all items
    for my_integer in my_integer_list:
        my_sumSqDiff_list_total = my_sumSqDiff_list_total + (my_integer - my_list_average)**2 
        #print(f'my list total: {my_sumSqDiff_list_total}')
    
    
    print(f'sum square difference list total is: {my_sumSqDiff_list_total}. ')
    #Returning the sum square difference list total
    return my_sumSqDiff_list_total

#Initializing the list of integers for finding the standard deviation
integer_list=[12, 23, 54, 23, 56, 78, 89, 93, 45, 31]
#Printing the list to the console for user info
print(f'list: [12, 23, 54, 23, 56, 78, 89, 93, 45, 31]')
#Calling the function to get the average for the items in the list
list_average = calculate_Avg(integer_list)
#Calling the function to calculate the sum square difference of the previous list such integer list and list average
sumSqDiff_list_total=calculate_sumSqDiff(integer_list, list_average)
#Printing out the value of the standard deviation
print(f'standard deviation = {math.sqrt(sumSqDiff_list_total/len(integer_list))}')


        
