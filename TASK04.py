import json
import csv

#write data.txt
with open("data.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")

#read data.txt
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

#convert to json
with open("data.json", "w") as file:
    lines = content.strip().split('\n')
    json.dump(lines, file, indent=4)

#convert to csv
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    lines = content.strip().split('\n')
    for line in lines:
        writer.writerow([line])
