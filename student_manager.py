import json
import csv
import os

students = [
    {'StudentId': 'S002', 'Name': 'John Doe', 'Math': 85, 'Science': 90, 'English': 88},
    {'StudentId': 'S003', 'Name': 'Jane Smith', 'Math': 92, 'Science': 89, 'English': 94},
]

if not os.path.exists('students.csv'):
    with open('students.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['StudentId', 'Name', 'Math', 'Science', 'English', 'Average'])
        writer.writeheader()
        for student in students:
            scores = [int(student["Math"]), int(student["Science"]), int(student["English"])]
            average = round(sum(scores) / len(scores),2)
            student['Average'] = average
            writer.writerow(student)

def menu():
    print("Menu:")
    print("1. Add student")
    print("2. View all students")
    print("3. Calculate statistics")
    print("4. Search student")
    print("5. Update student scores")
    print("6. Export to JSON")
    print("7. Export to CSV")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    return choice 

def add_student():
    input_student_id = input("Enter student ID (number only): ")
    n = 3 - len(input_student_id)
    id = 'S' + input_student_id.zfill(n)
    name = input("Enter student name: ")
    math_score = int(input("Enter Math score (0-100): "))
    sci_score = int(input("Enter Science score (0-100): "))
    eng_score = int(input("Enter English score (0-100): "))
    with open('students.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['StudentId', 'Name', 'Math', 'Science', 'English', 'Average'])
        scores = [int(student["Math"]), int(student["Science"]), int(student["English"])]
        average = round(sum(scores) / len(scores),2)
        writer.writerow({'StudentId': id, 'Name': name, 'Math': math_score, 'Science': sci_score, 'English': eng_score, 'Average': average})
    students.sort(key=lambda x: x['StudentId'])
    print('-'*50)
    print("Student added successfully!")
    print('-'*50)


def view_all_students():
    print("All students:")
    print('-'*50)
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        student_list = list(reader)
        student_list.sort(key=lambda x: x['StudentId'])
        print('StudentId\tName\tMath\tScience\tEnglish\tAverage')
        for student in student_list:
            print(f"{student['StudentId']}\t{student['Name']}\t{student['Math']}\t{student['Science']}\t{student['English']}\t{student['Average']}")
    print('-'*50)

def calculate_statistics():
    print("Statistics:")
    print('-'*50)
    with open('students.csv', 'r') as file:
        num_students = sum(1 for line in file) - 1
        for student in students:
            eng_score_avg = sum(int(student['English']) for student in students)/num_students
            math_score_avg = sum(int(student['Math']) for student in students)/num_students
            sci_score_avg = sum(int(student['Science']) for student in students)/num_students
            highest_math_score = max(int(student['Math']) for student in students)
            highest_sci_score = max(int(student['Science']) for student in students)
            highest_eng_score = max(int(student['English']) for student in students)
            lowest_math_score = min(int(student['Math']) for student in students)
            lowest_sci_score = min(int(student['Science']) for student in students)
            lowest_eng_score = min(int(student['English']) for student in students)
            if highest_math_score == student['Math']:
                highest_math_student = student['Name']
            if highest_sci_score == student['Science']:
                highest_sci_student = student['Name']
            if highest_eng_score == student['English']:
                highest_eng_student = student['Name']
            if lowest_math_score == student['Math']:
                lowest_math_student = student['Name']
            if lowest_sci_score == student['Science']:
                lowest_sci_student = student['Name']
            if lowest_eng_score == student['English']:
                lowest_eng_student = student['Name']

    print(f"Total number of students: {num_students}")
    print('-'*50)
    print(f"Average Math score: {math_score_avg:.2f}")
    print(f"Average Science score: {sci_score_avg:.2f}")
    print(f"Average English score: {eng_score_avg:.2f}")
    print('-'*50)
    print('Highest scores:')
    print(f"Math: {highest_math_score} ({highest_math_student})")
    print(f"Science: {highest_sci_score} ({highest_sci_student})")
    print(f"English: {highest_eng_score} ({highest_eng_student})")
    print('-'*50)
    print('Lowest scores:')
    print(f"Math: {lowest_math_score} ({lowest_math_student})")
    print(f"Science: {lowest_sci_score} ({lowest_sci_student})")
    print(f"English: {lowest_eng_score} ({lowest_eng_student})")
    print('-'*50)

def search_student(students, query):
    results = []
    for student in students:
        if query.lower() in student["Name"].lower() or query == student["StudentID"]:
            results.append(student)
    return results

def update_student_scores():
    student_id = input("Enter student ID to update: ")
    students_list = []
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        students_list = list(reader)
    
    for student in students_list:
        if student['StudentId'] == student_id:
            new_math_score = input("Enter new Math score (0-100): ").strip()
            new_sci_score = input("Enter new Science score (0-100): ").strip()
            new_eng_score = input("Enter new English score (0-100): ").strip()
            if new_math_score:
                student['Math'] = new_math_score
            if new_sci_score:
                student['Science'] = new_sci_score
            if new_eng_score:
                student['English'] = new_eng_score
            scores = [int(student["Math"]), int(student["Science"]), int(student["English"])]
            student['Average'] = str(round(sum(scores) / len(scores), 2))
            with open('students.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['StudentId', 'Name', 'Math', 'Science', 'English', 'Average'])
                writer.writeheader()
                writer.writerows(students_list)
            print("Student scores updated successfully!")
            return
    print("Student not found!")

def export_to_json():
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        students_list = list(reader)
        with open('students.json', 'w') as file:
            json.dump(students_list, file, indent=4)
    print("Data exported to students.json successfully!")

def export_to_csv():
    print("Data exported to students.csv successfully!")

while True: 
    try:
        choice = menu()
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        continue
    if choice < 1 or choice > 8:
        print("Invalid input. Please enter a number between 1 and 8.")
        continue
    if choice == 1:
        add_student()
    elif choice == 2:
        view_all_students()
    elif choice == 3:
        calculate_statistics()
    elif choice == 4:
        search_student()
    elif choice == 5:
        update_student_scores()
    elif choice == 6:
        export_to_json()
    elif choice == 7:
        export_to_csv()
    elif choice == 8:
        print('Thank you for using the Student Manager. Goodbye!')
        break 
    