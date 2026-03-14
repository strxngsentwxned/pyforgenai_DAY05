import json 

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
        "salary": 50000,
        "years_of_experience": 5
    }
]

with open("employee_data.json", "w") as file:
    json.dump(employee_data, file, indent=4)
