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

while True:
  print("Add item pls")

  with open("todo.txt", "a") as file:
    new_item = input("what do you want to do?")
    file.write(f"{new_item} \n")

  with open("todo.txt", "r") as file:
    lines = file.readlines()
    print("\n Updated list: \n")
    for i, lines in enumerate(lines,1):
      print(f"{i}. {lines.strip()}")
	
	
