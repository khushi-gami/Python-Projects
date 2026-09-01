# print welcome message..
print("Welcome to the Pattern Generator and Number Analyzer !")

print()

# loop tb tk chalta rhega jb tk break na ho..
while True:

    print()
   
   # print choices list..
    print("Select an option : ")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    print()

    # enter a choice..
    choice = int(input("Enter your choice (1/2/3) : "))

    print()
    # if user enter choice 1 then this code will run..
    if choice == 1:
        
        # user enter no. of rows , user ko jitne rows ka pattern chahiye..
        rows = int(input("Enter the number of rows for the pattern : "))
        
        # if user enter invalid values for rows , then take this value second time from the user..
        if rows <= 0:

            # this message will show , when user enter invalid no. of rows (0 ya -ve)..
            print("Invalid nummber of rows enterted..!")
            rows = int(input("Please Enter valid (positive) number of rows for the pattern : "))
        
        print()

        print("Pattern :")

        # logic of print pattern..
        for i in range(1,rows+1):
            for j in range(i):
                print("*" , end =" ")
            print()

    # if user enter choice 2 then this code will run..
    elif choice == 2:
        start_num = int(input("Enter the start of the range : "))
        end_num = int(input("Enter the end of the range : "))
        
        # if user enter end number less than start number , at that time - again take end number..
        if end_num <= start_num:
            print("End number is always higher than start number !")
            end_num = int(input("Enter valid end of the range : "))

        # starting value of sum
        total = 0

        # logic of print even or odd number given by the user
        for i in range(start_num,end_num+1):
            if i % 2 == 0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")
            # sum of all the numbers criteria given by the user
            total +=i

        # print sum of all numbers
        print(f"Sum of all numbers from {start_num} to {end_num} is : ",total)
   
    # if user enter choice 3 then this code will run..
    elif choice == 3 :

        print("Exiting the program. Goodbye !")
        # here loop will break
        break

    # if user enter invalid choice , at that time print error..
    else:
        print("Invalid Choice Enterted !")

        print()
        # skip this iteration and move on next iteration..
        continue







    
    











