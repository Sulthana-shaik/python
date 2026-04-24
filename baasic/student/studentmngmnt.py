#students =[] #list to store student dictinaies

#def add_student():
# student_id = input("Enter student ID: ")
#   name = input("Enter student name: ")
#   students.append({'id': student_id, 'name': name})
#   print("Student added sucessfully!")
# def view_students():
#   if not students:
#       print("No studentd found.")      return
#  print("Student List:")  for student in students:
# print(f"ID: {student['id']}")
students = []

# Helper function
def find_student(student_id):
    for student in students:
        if student['id'] == student_id:
            return student
    return None


# ADD
def add_student():
    student_id = input("Enter Student ID: ")

    if find_student(student_id):
        print("ID already exists!\n")
        return

    name = input("Enter Student Name: ")
    students.append({'id': student_id, 'name': name})
    print("Student Added Successfully\n")


# VIEW
def view_students():
    if not students:
        print("No Students found.\n")
        return 
    print("Student List:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}")
    print()


# UPDATE
def update_student():
    student_id = input("Enter student ID to update: ")
    student = find_student(student_id)

    if student:
        student['name'] = input("Enter new name: ")
        print("Student updated successfully\n")
    else:
        print("Student not found.\n")


# DELETE
def delete_student():
    student_id = input("Enter student ID to delete: ")
    student = find_student(student_id)

    if student:
        students.remove(student)
        print("Student deleted successfully\n")
    else:
        print("Student not found.\n")


# SEARCH
def search_student():
    student_id = input("Enter student ID to search: ")
    student = find_student(student_id)

    if student:
        print(f"Student Found -> ID: {student['id']}, Name: {student['name']}\n")
    else:
        print("Student not found.\n")


# MAIN
def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()