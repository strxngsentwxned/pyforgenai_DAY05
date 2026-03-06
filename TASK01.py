with open("todo.txt", "w") as file:
	file.write("homework")
	file.write("ppt")
	file.write("correction")
	file.write("study")
	file.write("eat")

with open("todo.txt", "r") as file:
	lines = file.readlines()
	for i, lines in enumerate(range(lines,1)):
		print(f"{i}). {lines.strip()}")

print("Add item pls")

with open("todo.txt", "a") as file:
	file.write(input("what do you want to do?"))

with open("todo.txt", "r") as file:
	content = file.read()
	print("Updated List:")
	print(content)
	
	

