# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Moriah Tillman,11/09/2026,Modified Script
#   Moriah Tillman,11/10/2026,Modified Script
#   Moriah Tillman,11/11/2026,Modified Script
#   Moriah Tillman,11/12/2026,Modified Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}  # a dictionary
students: list = []
file = None
menu_choice: str = ''

# When program starts, read existing registrations
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data

while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    print()
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if student_first_name == '':
                raise ValueError("The first name should not be blank.")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if student_last_name == '':
                raise ValueError("The last name should not be blank.")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            if course_name == '':
                raise ValueError("The course name should not be blank.")

            #store student information in the dictionary
            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            students.append(student_data)
            print(f"You have registered "
                  f"{student_first_name} "
                  f"{student_last_name} for "
                  f"{course_name}."
                  )
        except ValueError as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue
# Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} "
                  f"{student['LastName']} "
                  f"is enrolled in "
                  f"{student['CourseName']}"
                  )
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = None

        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)

            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} "
                      f"{student['LastName']} "
                      f"is enrolled in "
                      f"{student['CourseName']}"
                      )
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        # Check if a file object exists and is still open
        finally:
            if file is not None and file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
