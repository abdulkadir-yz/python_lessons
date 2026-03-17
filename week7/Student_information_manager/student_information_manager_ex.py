from datetime import datetime
students = []
available_courses = {"math", "science", "history", "english", "art", "music"}

def add_student():
    print("\n--------Add a New Student---------")
    name = input("Enter student name: ").strip().title() # Taking input for student name and formatting it
    # input() get information from the user and store it in the variable name
    # strip() removes any leading or trailing whitespace from the input e.g. "  John  " becomes "John"
    # title() converts the first character of each word to uppercase and the rest to lowercase e.g. "john doe" becomes "John Doe"
    # First input() , after strip() and lastly after title() is stored in the variable name, this is "method chaining" 
    while True: # Why first "while True:" ? Because we want to keep asking the user for input until they provide valid input
        age_input = input("Enter student age(15-20): ").strip() # Taking input for student age and formatting it
        if not age_input.isdigit(): # Checking if the input is a digit or not, if not we ask the user to enter a valid age
            # isdigit() checks if all the characters in the string are digits, if not it returns False, if it is a digit it returns True
            print("Invalid input. Please enter a number for age.")
            continue # continue is used to skip the rest of the code in the loop and go back to the beginning of the loop to ask for input again
        age = int(age_input) # Converting the input to an integer 
        # int() converts the string input to an integer, if the input is not a valid integer it will raise a ValueError, but we have already checked if the input is a digit or not, so we can safely convert it to an integer
        if age < 15 or age > 20: # Checking if the age is between 15 and 20, if not we ask the user to enter a valid age
            print("Invalid age. Please enter an age between 15 and 20.")
            continue
        break # If the age is valid, we break out of the loop
    print("Available courses: " + ", ".join(sorted(available_courses))) # Showing the available courses to the user

    while True: # We want to keep asking the user for input until they provide valid input
        courses_input = input("Enter courses (comma separated): ").strip() # Taking input for student courses and formatting it
        courses = [c.strip() for c in courses_input.lower().split(",") if c.strip()] # Converting the input to a list of courses, and formatting it
        # lower() converts the input to lowercase, split(",") splits the input into a list of courses based on the comma separator, 
        # and the list comprehension [c.strip() for c in courses_input.lower().split(",")] removes any leading or trailing whitespace from each course in the list
        # 1) course_input.lower().split(",") takes the input string, converts it to lowercase, and splits it into a list of courses based on the comma separator.
        #  For example, if the input is "Math, Science, History", it becomes ["math", " science", " history"].
        # 2) "for c in ..." iterates through each course in the list created in step 1. In our example, it will iterate through "math", " science", and " history".
        # 3) "c.strip()" removes any leading or trailing whitespace from each course. In our example, it will convert " science" to "science" and " history" to "history".
        # 4) "if c.strip()" is a condition that checks if the stripped course is not an empty string. This ensures that if the user accidentally enters extra commas 
        # (e.g, "Math, , Science") it will be ignored.
        if len(courses) == 0: # Checking if the user entered any courses or not, if not we ask the user to enter at least one course
            print("Please enter at least one course.")
            continue
        invalid_courses = [c for c in courses if c not in available_courses] # Checking if the courses entered by the user are valid or not, if not we ask the user to enter valid courses
        if invalid_courses: # If there are any invalid courses, we show the user which courses are invalid and ask them to enter valid courses
            print("These courses are not available: " + ", ".join(invalid_courses))
            print("Please choose from: " + ", ".join(sorted(available_courses)))
            continue
        if len(set(courses)) < len(courses):
            # SET() is a built-in data type in Python that represents an unordered collection of unique elements. 
            # When we convert the list of courses to a set, it will remove any duplicate courses. 
            # If the length of the set of courses is less than the length of the original list of courses, it means that there were duplicate courses in the original list.
            # For example, if the user enters "Math, Science, Math", the list of courses will be ["math", "science", "math"], and the set of courses will be {"math", "science"}.   
            print("You entered duplicate courses. Please enter each course only once.")
            continue
        break # If the courses are valid, we break out of the loop
    student = {
        "name": name,
        "age": age,
        "courses": tuple(courses)
    }
    # tuple() is a built-in data type in Python that represents an ordered collection of elements.
    # We are converting the list of courses to a tuple because we want to make it immutable,
    # meaning that once we create the student dictionary, we don't want to change the courses of the student.
    students.append(student.copy()) # Adding the student to the list of students, we use copy() to create a copy of the student dictionary, so that if we change the student dictionary later, it won't affect the student in the list of students
    print(f"Student {name} added successfully!")

def view_all_students():
    print("\n--------All Students---------")
    if not students: # Checking if there are any students in the list of students, if not we show a message to the user and ask them if they want to add a student now
        print("No students added yet")
        answer = input("Do you want to add a student now? (yes/no): ").strip().lower() # Asking the user if they want to add a student now, and formatting the input
        if answer == "yes": # If the user wants to add a student now, we call the add_student() function to allow them to add a student
            add_student()
        else:
            input("Press Enter to return to the main menu.")
        return  
    for i, s in enumerate(students, start=1): # i = index of the student in the list of students, s = student dictionary, start=1 means that the index will start from 1 instead of 0
        # enumerate() is a built-in function in Python that adds a counter to an iterable and returns it as an enumerate object.
        # In this case, we are using enumerate() to get the index of each student in the list of students, starting from 1.
        # For example, if we have 3 students in the list of students, the enumerate() function will return (1, student1), (2, student2), (3, student3).
        print(f"\nStudent {i}:") # Showing the index of the student in the list of students, we use f-string to format the output
        print(f"  Name: {s['name']}") # Showing the name of the student, we access the name of the student from the student dictionary using s['name'] and format it using f-string
        print(f"  Age: {s['age']}") # Showing the age of the student, we access the age of the student from the student dictionary using s['age'] and format it using f-string
        print(f"  Courses: {', '.join(s['courses'])}") # Showing the courses of the student, we access the courses of the student from the student dictionary using s['courses'],
        # which is a tuple of courses, and we use join() to join the courses into a single string separated by commas, and format it using f-string

    input("\nPress Enter to return to the main menu.")
    return

def search_student():
    print("\n--------Search for a Student---------")
    search_name = input("Enter student name to search: ").strip().title() # Taking input for student name and formatting it
    found = False # We need to create a variable to check if the student is found or not
    for s in students: # Looping through the list of students
        if s["name"] == search_name: # Checking if the name of the student matches the search name
            print(f"\nStudent found:")
            print(f"  Name: {s['name']}")
            print(f"  Age: {s['age']}")
            print(f"  Courses: {', '.join(s['courses'])}")
            found = True
            break # If the student is found, we break out of the loop
    if not found: # If the student is not found, we show a message to the user
        print(f"Student {search_name} not found.")
    input("\nPress Enter to return to the main menu.")
    return
def show_statistics():
    print("\n--------Statistics---------")
    total_students = len(students) # Getting the total number of students by using the len() function on the list of students
    print(f"Total number of students: {total_students}") # Showing the total number of students
    all_enrolled_courses = set() # We need to create a set to store the unique courses enrolled by the students
    for s in students: # For each student in the list of students, we want to count the number of students in each course
        for course in s["courses"]: # For each course in the course of the studenrt
            all_enrolled_courses.add(course) # We add the course to the set of all enrolled courses, we use a set because we want to have unique courses only 
            # add() is a method of the set data type that adds an element to the set, if the element is already in the set, it won't be added again, so we will have unique courses only
    if all_enrolled_courses: # If there are any enrolled courses, we show the number of students in each course
        print(f"Unique courses enrolled: {', '.join(sorted(all_enrolled_courses))}") # Showing the unique courses enrolled, we use sorted() to sort the courses alphabetically
    else : # If there are no enrolled courses, we show a message to the user
        print("No courses enrolled yet.")
    course_counts = {}
    print("\nStudents per course:")

    for course in sorted(available_courses):
        count = 0
        for s in students:
            if course in s["courses"]:
                count += 1
        course_counts[course] = count
        print(f"  {course}: {count} students")
    if course_counts and total_students > 0:
        max_count = max(course_counts.values())
        min_count = min(course_counts.values())
        highest = [c for c, count in course_counts.items() if count == max_count]
        lowest = [c for c, count in course_counts.items() if count == min_count]
        print(f"\nMost popular course(s): {', '.join(sorted(highest))}")
        print(f"Least popular course(s): {', '.join(sorted(lowest))}")
    empty_courses = available_courses - all_enrolled_courses # We can find the empty courses by taking the difference between the set of available courses and the set of all enrolled courses
    if empty_courses: # If there are any empty courses, we show the empty courses to the user
        print(f"\nEmpty courses: {', '.join(sorted(empty_courses))}")
    else: # If there are no empty courses, we show a message to the user
        print("\nNo empty courses.")
    input("\nPress Enter to return to the main menu.")
    return

while True: # We want to keep showing the main menu until the user chooses to exit
    print("\n--------Student Information Manager---------")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Show statistics")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip() # Taking input for the user's choice and formatting it
    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_statistics()
    elif choice == "5":
        confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower() # Asking the user to confirm if they want to exit, and formatting the input
        if confirm == "yes":
            print("Exiting the program. See you next time")
            break # If the user confirms that they want to exit, we break out of the loop and end the program
        else:
            print("Returning to the main menu.")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")