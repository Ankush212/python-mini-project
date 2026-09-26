# Student Record Management System

A simple **console-based Student Record Management System** developed using **Python**.

This project allows the user to manage student records through a simple menu-driven console application.

## Features

The application provides the following options:

1. **Add Student**

   * Add a new student record.
   * Enter Student ID, Name, Age, Course, Marks, and Phone Number.
   * Checks whether the Student ID already exists.

2. **View All Students**

   * Displays all student records.
   * Shows a message if there are no records.

3. **Search Student**

   * Search for a student using the Student ID.
   * Displays the student's details if the record is found.

4. **Update Student**

   * Update the details of an existing student.
   * Student ID is used to find the record.
   * Empty fields can be left unchanged.

5. **Delete Student**

   * Delete a student record using the Student ID.

6. **Exit**

   * Closes the application.

## Technologies Used

* **Python 3**
* Python Lists
* Python Dictionaries
* Functions
* `if-elif-else` statements
* `for` and `while` loops
* `input()` and `print()`

No external libraries are required.

## Project Structure

```text
Student-Record-Management/
│
├── student_record.py
└── README.md
```

* `student_record.py` - Main Python program.
* `README.md` - Project documentation.

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

You can check it by opening a terminal or command prompt and running:

```bash
python --version
```

### Step 2: Open the Project

Open the project folder in an editor such as VS Code.

### Step 3: Run the Program

Run the following command in the terminal:

```bash
python student_record.py
```

The application will display the main menu.

## Main Menu

The program displays:

```text
================================
   STUDENT RECORD MANAGEMENT
================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
================================
```

Enter a number from **1 to 6** to perform an operation.

## Example

### Adding a Student

```text
--- Add Student ---

Enter Student ID: 101
Enter Name: Ankush
Enter Age: 20
Enter Course: MCA
Enter Marks: 85
Enter Phone Number: 9876543210

Student added successfully!
```

### Viewing Students

```text
--- All Student Records ---

----------------------------
Student ID : 101
Name       : Ankush
Age        : 20
Course     : MCA
Marks      : 85
Phone      : 9876543210
```

### Searching for a Student

```text
--- Search Student ---

Enter Student ID to search: 101

Student Found!
----------------------------
Student ID : 101
Name       : Ankush
Age        : 20
Course     : MCA
Marks      : 85
Phone      : 9876543210
```

## How the Program Stores Data

The program uses a Python **list** to store student records:

```python
students = []
```

Each student is stored as a **dictionary** containing their information:

```python
student = {
    "id": student_id,
    "name": name,
    "age": age,
    "course": course,
    "marks": marks,
    "phone": phone
}
```

The student is then added to the list using:

```python
students.append(student)
```

## Functions Used

The program is divided into separate functions to make the code easier to understand.

### `add_student()`

Adds a new student to the list.

### `view_students()`

Displays all student records.

### `search_student()`

Searches for a student using their Student ID.

### `update_student()`

Updates the details of an existing student.

### `delete_student()`

Removes a student from the list.

## Important Note

This is a **basic console-based project** designed for learning Python programming.

The student records are stored only while the program is running. Since the current version does not use a database or file storage, **all records will be lost when the program is closed**.

## Learning Objectives

This project helps beginners understand:

* How to use Python lists
* How to use dictionaries
* How to create and call functions
* How to use loops
* How to use conditional statements
* How to take input from users
* How to add, search, update, and delete data
* How to create a menu-driven console application

## Future Improvements

The project can be improved in the future by adding:

* Save records to a file
* Load records when the program starts
* Input validation
* Better formatted student tables
* Sorting student records
* Search by student name
* Calculate grades from marks
* Use a database such as SQLite

## Author

**Student Record Management System**

Developed as a Python mini project.
