import os

students = ['John Snow', "Bernie Sanders"]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
#######################
Year 10 Class List Menu
#######################

Type:
 - ADD to add a new student
 - SHOW to output the current class list
 - UPDATE to update an existing student
 - REMOVE to remove a student from the class list
 - EXIT to end the program
''')
    selection = str(input("Selection: "))

    if selection.lower() == "add":
        name = str(input("\nStudents Name: "))
        students.append(name)

    elif selection.lower() == "show":
        print("\nStudents:")
        for student in students:
            print(student)
        print()    
        input("Press enter to continue")

    elif selection.lower() == "remove":
        name = input("\nStudents Name: ")

        try:
            students.remove(name)

        except ValueError:
            print("Name not in list!")

    elif selection.lower() == "update":
        name = input("\nStudents Name: ")
        newName = input("Students new Name: ")

        try:
            students[students.index(name)] = newName

        except ValueError:
            print("Student Non-Existent")

    elif selection.lower() == "exit":
        break

