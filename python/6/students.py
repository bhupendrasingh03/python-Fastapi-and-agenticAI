# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         # print(row)
#         print(f"{row[0]} is in row {row[1]}")

# Notice that rstrip removes the end of each line in our CSV file. split tells the interpreter where to find the end of each of our values in our CSV file. row[0] is the first element in each line of our CSV file. row[1] is the second element in each line in our CSV file.

# The above code is effective at dividing each line or “record” of our CSV file. However, it’s a bit cryptic to look at if you are unfamiliar with this type of syntax. Python has built-in ability that could further simplify this code. Modify your code as follows:

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
# Notice that the split function actually returns two values: The one before the comma and the one after the comma. Accordingly, we can rely upon that functionality to assign two variables at once instead of one!

# Imagine that we would again like to provide this list as sorted output? You can modify your code as follows:



# ======================//
# Python’s built-in csv library comes with an object called a reader. As the name suggests, we can use a reader to read our CSV file despite the extra comma in “Number Four, Privet Drive”. A reader works in a for loop, where each iteration the reader gives us another row from our CSV file. This row itself is a list, where each value in the list corresponds to an element in that row. row[0], for example, is the first element of the given row, while row[1] is the second element.

# import csv
# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name":row[0], "home":row[1]})
        
# for student in sorted(students, key=lambda student:student['name']):
#     print(f"{student['name']} is from {student['home']}")
    
    
    # We can modify our code to use a part of the csv library called a DictReader to treat our CSV file with even more flexibilty:
    

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")
    
# Notice that we have replaced reader with DictReader, which returns one dictionary at a time. Also, notice that the interpreter will directly access the row dictionary, getting the name and home of each student. This is an example of coding defensively. As long as the person designing the CSV file has inputted the correct header information on the first line, we can access that information using our program.


# ================================// ===================//
# Up until this point, we have been reading CSV files. What if we want to write to a CSV file?

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv",'a') as file:
    writer = csv.DictWriter(file,fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})
    
    
