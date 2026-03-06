with open("todo.txt", "w") as file:
	file.write("homework")
	file.write("ppt")
	file.write("correction")
	file.write("study")
	file.write("eat")

with open("todo.txt", "r") as file:
	content = file.read()
	print(content)
	
	
