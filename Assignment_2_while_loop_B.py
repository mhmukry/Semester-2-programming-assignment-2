#b)	Use version management with git and make the following changes to the program in part a:
#The loop breaks if the user types your student number print the message “ cutoff point”. 
#The loop should skip the statements in current iteration and does not increment count whenever 
# the user types a multiple of 11. Flowchart is required for this program.
loop_iteration_value = 0
student_number = 991798855
loop_variable = True
while (loop_variable):
    user_input = int(input("Enter your number: "))
    if user_input % 11 != 0:
        if user_input == student_number:
            print(f'cutoff point: student_number =  {user_input}')
            break
        loop_iteration_value = loop_iteration_value + 1
        print(f'iteration number: {loop_iteration_value}')
        if user_input < 0:
            loop_variable = False
            print(f'user entered value: {user_input} is a negative value. Exiting the program.')

        else:
            print(f'user entered value: {user_input}')
            
    else:
        print(f'user input: {user_input} is a multiple of 11. Skipping all the statements in the current iteration. ')
