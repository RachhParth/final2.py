students = []  

def add_student():
    print("\nEnter student details:")
    student = {}
    student["id"] = input("Student ID: ")
    student["name"] = input("Name: ")
    student["age"] = input("Age: ")
    student["grade"] = input("Grade: ")
    student["dob"] = input("Date of Birth (YYYY-MM-DD): ")
    subjects = input("Subjects (comma-separated): ")
    student["subjects"] = [s.strip() for s in subjects.split(",")]

    students.append(student)
    print("\nStudent added successfully!")

def display_students():
    if not students:
        print("\nNo students found.")
    else:
        print("\n--- Display All Students ---")
        for s in students:
            print(f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | "
                  f"Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}")

def update_student():
    sid = input("\nEnter Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            print("Leave blank if no change.")
            name = input("New Name: ")
            age = input("New Age: ")
            grade = input("New Grade: ")
            dob = input("New Date of Birth (YYYY-MM-DD): ")
            subjects = input("New Subjects (comma-separated): ")

            if name: s["name"] = name
            if age: s["age"] = age
            if grade: s["grade"] = grade
            if dob: s["dob"] = dob
            if subjects: s["subjects"] = [sub.strip() for sub in subjects.split(",")]

            print("Student updated successfully!")
            return
    print("Student not found!")

def delete_student():
    sid = input("\nEnter Student ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found!")

def display_subjects():
    all_subjects = set()
    for s in students:
        all_subjects.update(s["subjects"])
    if all_subjects:
        print("\nSubjects Offered:", ", ".join(all_subjects))
    else:
        print("\nNo subjects found.")

def menu():
    print("\nWelcome to the Student Data Organizer!")
    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_subjects()
        elif choice == "6":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
