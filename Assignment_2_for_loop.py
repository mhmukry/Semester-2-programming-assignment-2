import math #Importing math module to use square root function

#Initializing the dimension list and vector value
dimension_list = [0,0,0]
total_square_value_of_dimensions = 0

#Using for loop to get the user input value to reset dimension list value and calculate the square for the dimension values entered 
for dimension_value in dimension_list:
    dimension_value += int(input("Enter the value for the dimension: "))
    total_square_value_of_dimensions += dimension_value**2
    #print(f'total_square_value_of_dimensions : {total_square_value_of_dimensions }')
#Finding the square root for |M|= √(x^2+y^2+z^2) 
vector_value = math.sqrt(total_square_value_of_dimensions )
print(f'Magnitude of vectors is |M|= {vector_value}')

