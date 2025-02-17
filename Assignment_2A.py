
#Taking user input
user_input = int(input("Enter the number of rows: "))
#Using for loop to print the row for the desired character
for i in range(1,user_input+1):
    #Checking if row number is even or odd
    if (i % 2 == 0):
        #Padding space to print the character according to the requested format
        print((user_input - i)*" ",(2*i-1)*"+")
    else:
        print((user_input - i)*" ",(2*i-1)*"*")



