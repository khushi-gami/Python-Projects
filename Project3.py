
print("Welcome to the Student Data Organizer!")

print()

# for collecting information..
student_ids = set()
student_details = []

while True:
   
    print("Select an option : ")

    print()

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    print()

    choice = int(input("Enter your choice (1/2/3/4/5/6) : "))

    print()

    # |||||||||||||||||||||||||||||||   ADD STUDENT |||||||||||||||||||||||||||||||||||
   
    if choice == 1 :

        print("Enter student details :")

        new_id = int(input("Student ID : "))

        if new_id in student_ids:

            print()

            print("This ID is already exists!")

            print()

        else:

           # store data in dictionary
            student = {
                new_id:{
                "Name" : input("Name : "),
                "Age" :int(input("Age : ")),
                "Grade" :input("Grade : "),
                "Date of Birth" : input("Date of Birth (YYYY-MM-DD) : "),
                "Subjects" : set(input("Subjects (comma-separated) : ").split(","))
                }
            }

            student_ids.add(new_id)
            student_details.append(student)
        
            print()
    
            print("Student added Successfully!")
    
            print()

    # |||||||||||||||||||||||||||||||   SHOW STUDENTS  ||||||||||||||||||||||||||||||

    elif choice == 2 :

        print("All Students List : ")

        print()

        for student in student_details:

            for student_id,details in student.items():
            
                print(f"Student ID : {student_id} | Name : {details['Name']} | Age : {details['Age']} | Grade : {details['Grade']} | Subjects : {details['Subjects']}")

            print()

    # |||||||||||||||||||||||||   UPDATE STUDENT INFORMATION  ||||||||||||||||||||||||

    elif choice == 3 :

        update_student_id = int(input("Enter Student ID to update : "))

        print()
        
        if update_student_id in student_ids:

            for student in student_details:

                if update_student_id in student:   

                    details = student[update_student_id]  
              
                    print("What do you update ?")
                    print("1. Age")
                    print("2. Subjects")
                    print("3. Both")
                    update_choice = int(input("Enter a option to update (1/2/3) : "))

        # ---------------------- Update student AGE -----------------------------

                    if update_choice == 1:

                        print()

                        print("Enter new value of :")

                        update_age = int(input("Age : "))
        
                        print()
        
                        details["Age"] = update_age
        
                        print("Age updated Successfully !")
        
                        print()
            
        # ---------------------- Update student SUBJECTS -----------------------------

                    elif update_choice == 2:

                        print()

                        print("Enter new values of :")

                        update_subjects = set(input("subjects (comma-separated) : ").split(","))
        
                        print()
        
                        details["Subjects"] = update_subjects
        
                        print("Subjects Updated Successfully !")
        
                        print()

        # -------------------- Update student AGE & SUBJECTS ----------------------

                    elif update_choice == 3:

                        print()

                        print("Enter new values of :")

                        update_age = int(input("Age : "))
                        update_subjects = set(input("Subjects (comma-separated) : ").split(","))
        
                        print()
            
                        details["Age"] = update_age
                        details["Subjects"] = update_subjects
                        
                        print("Age and Subjects Updated Successfully !")
        
                        print()
                    
                    break 

        else:
            print(f"{update_student_id} Student ID does not exist!")
        
            print()

    # |||||||||||||||||||||||||||||||   DELETE STUDENT  ||||||||||||||||||||||||||||||

    elif choice == 4:
  
        delete_student_id = int(input("Enter Student ID to delete : "))

        print()
        
        if delete_student_id in student_ids:

            for index,student in enumerate(student_details):

                if delete_student_id in student:  

                    del student_details[index]
                    student_ids.remove(delete_student_id)

                    print("Student Delete Successfully!")

                    print()

                    break

        else:

            print("Student ID does not exist!") 

            print()

    # |||||||||||||||||||||||||||   DISPLAY ALL SUBJECTS  |||||||||||||||||||||||||||


    elif choice == 5:

        print("Display Subjects Offered : ")

        print()

        subjects = set()

        for student in student_details:

            for details in student.values():

                subjects.update(details["Subjects"])

        print(subjects)
            
        print()

    # |||||||||||||||||||||||||||||||   EXIT PROGRAMME  ||||||||||||||||||||||||||||||

    elif choice == 6:

        print("Exiting the program..!")
        
        break
            
    else:

        print("Invalid Choice Enterted !")

        print()
 
        continue







    
    











