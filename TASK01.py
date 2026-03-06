with open("todo.txt", "w") as file:
	file.write("homework\n")
	file.write("ppt \n")
	file.write("correction \n")
	file.write("study \n")
	file.write("eat \n")

with open("todo.txt", "r") as file:
	lines = file.readlines()
	for i, lines in enumerate(lines,1):
		print(f"{i}). {lines.strip()}")

print("Add item pls")

with open("todo.txt", "a") as file:
	file.write(input("what do you want to do?"))

with open("todo.txt", "r") as file:
	lines = file.readlines()
	print("Updated list: \n")
	for i, lines in enumerate(lines,1):
		print(f"{i}. {lines.strip()}")
	
	

