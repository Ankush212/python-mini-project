students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")
    phone = input("Enter Phone Number: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "phone": phone
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    print("\n--- All Student Records ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("----------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("Marks      :", student["marks"])
        print("Phone      :", student["phone"])


def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("----------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Marks      :", student["marks"])
            print("Phone      :", student["phone"])
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("Leave a field empty if you don't want to change it.")

            name = input("Enter new Name: ")
            age = input("Enter new Age: ")
            course = input("Enter new Course: ")
            marks = input("Enter new Marks: ")
            phone = input("Enter new Phone Number: ")

            if name != "":
                student["name"] = name

            if age != "":
                student["age"] = age

            if course != "":
                student["course"] = course

            if marks != "":
                student["marks"] = marks

            if phone != "":
                student["phone"] = phone

            print("Student record updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n================================")
    print("   STUDENT RECORD MANAGEMENT")
    print("================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Record Management System!")
        break

    else:
        print("Invalid choice! Please enter 1-6.")