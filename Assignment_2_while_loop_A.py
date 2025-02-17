
#Initializing the variable to zero
loop_iteration_value = 0
#Initializing the while loop variable to true
loop_variable = True

while (loop_variable):
    #Taking the user input as integer
    user_input = int(input("Enter the number: "))
    #Incrementing the loop iteration value
    loop_iteration_value = loop_iteration_value + 1
    print(f'iteration number: {loop_iteration_value}')
    #If user input is negative then setting the while loop variable to false to exit the program
    if user_input < 0:
        loop_variable = False
        print(f'user entered value: {user_input} is a negative number. Exiting the program.')
    else:
        print(f'user entered value: {user_input}')