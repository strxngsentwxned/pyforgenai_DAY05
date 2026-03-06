import json 

student_manager = {
	"students" : [
		{"name": "Alice", "age": 20, "grades": [85, 90, 88], "email": "87z9@gmail.com"},
		{"name": "Bob", "age": 19, "grades": [78, 82, 80], "email": "x78y@yahoo.com"},
	    {"name": "Charlie", "age": 21, "grades": [92, 95, 90], "email": "98a7@outlook.com"}
  	]
}

with open("students.json", "w") as file:
	json.dump(student_manager, file, indent =4)

#find average
with open("students.json", "r") as file:
	average_grades = []
	data = json.load(file)
	for student in data["students"]:
		grades = student["grades"]
		average = sum(grades)/len(grades)
		average_grades.append(average)
		print(f"{student['name']} average: {average}")
	highest_average = max(average_grades)
	highest_student = ""
	for name, avg in student_avg_map.items():
	    if avg == highest_average:
	        highest_student = name
	        break  
	print(f"{student["name"]} has the highest average of {highest_average}!")

 
for student in data["students"]:
	if student['name'] == "Charlie":
		student['grades'][1] = 93
		
#update score
with open("students.json", "w") as file:
	json.dumps(data, file, indent=4)
print(student_manager)


	
