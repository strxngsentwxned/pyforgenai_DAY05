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
    id = input("Enter student ID: ")
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
    print(f"Average Math score: {math_score_avg:.2f}")
    print(f"Average Science score: {sci_score_avg:.2f}")
    print(f"Average English score: {eng_score_avg:.2f}")
    print(f"Total number of students: {num_students}")

while True: 
    choice = menu()
    if choice == 1:
        add_student()
    elif choice == 2:
        view_all_students()
    elif choice == 3:
        calculate_statistics()