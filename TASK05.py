import json 
from collections import defaultdict
import csv

#write json file
employee_data = [
    {
        "name": "John Doe",
        "department": "Sales",
        "salary": 50000,
        "years_of_experience": 5
    },
    {
        "name": "Jane Doe",
        "department": "Marketing",
        "salary": 45000,
        "years_of_experience": 2
    },
    {
        "name": "Fred Smith",
        "department": "HR",
        "salary": 70000,
        "years_of_experience": 10
    },
    {
        "name": "John Doe",
        "department": "Sales",
        "salary": 30000,
        "years_of_experience": 3
    }
]

with open("employee_data.json", "w") as file:
    json.dump(employee_data, file, indent=4)


#find average by department
with open("employee_data.json", "r", encoding="utf-8") as f:
    employees = json.load(f)

sums = defaultdict(float)
counts = defaultdict(int)

for e in employees:
    dept = e["department"]
    salary = e["salary"]
    sums[dept] += salary
    counts[dept] += 1

avg_by_dept = {dept: sums[dept] / counts[dept] for dept in sums}

#find employees with more than 5 years of experience
experienced_employees = []
for employee in employee_data:
    if employee["years_of_experience"] >= 5:
        experienced_employees.append(employee["name"])

#calculate total payroll
total_payroll = 0
for employee in employee_data:
    total_payroll += employee["salary"]

#write as text
with open("report.txt", "w") as file:
    file.write("Average Salary by Department:\n")
    file.write(str(avg_by_dept)+"\n")
    file.write("Experienced Employees (5+ years):\n")
    file.write(str(experienced_employees)+"\n")
    file.write("Total Payroll:\n")
    file.write(str(total_payroll)+ "\n")

#write as csv, only experienced employees
with open("experienced_employees.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "department", "salary", "years_of_experience"])
    for employee in employee_data:
        if employee["years_of_experience"] >= 5:
            writer.writerow([employee["name"], employee["department"], employee["salary"], employee["years_of_experience"]])
