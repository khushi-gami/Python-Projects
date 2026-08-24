import datetime # For getting the current year
# print() & input() ------------------------------------------------------



print("Welcome to the Intractive personal Data Collector!")

print()

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
height = float(input("Please enter your height in meters : "))
favourite_number = int(input("Please enter your favourite number : "))

current_year = datetime.datetime.now().year
birth_year = int(current_year - age)

print()

print("Thank you! Here is the information we collected :")

print()

print(f"Name : {name}",type(name),"Memory Address :",id(name))
print(f"Age : {age}",type(age),"Memory Address :",id(age))
print(f"Height : {height}",type(height),"Memory Address :",id(height))
print(f"Favourite Number : {favourite_number}",type(favourite_number),"Memory Address :",id(favourite_number))

print()

print(f"Your birth year is approximately : {birth_year} (Based on your age {age})")

print()

print("Thank you for using the Personal Data Collector. Goodbye!")



