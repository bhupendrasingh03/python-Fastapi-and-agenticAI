# name = input("What's your name? ")
# print(f"hello, {name}")

# Notice that running this code has the desired output. The user can input a name. The output is as expected.

# However, what if we wanted to allow multiple names to be inputted? How might we achieve this? Recall that a list is a data structure that allows us to store multiple values into a single variable. Code as follows:

# names = []

# for _ in range(3):
#     names.append(input("What's your name?" ))
    
# Notice that the user will be prompted three times for input. The append method is used to add the name to our names list.

# names = []

# for _ in range(3):
#     names.append(input("What's your name? " ))

# for name in sorted(names):
#     print(f"hello, {name}")


# ============== open ==================
# open is a functionality built into Python that allows you to open a file and utilize it in your program. The open function allows you to open a file such that you can read from it or write to it.
# To show you how to enable file I/O in your program, let’s rewind a bit and code as follows:

# name = input("What's your name? ")
# file = open("names.txt", "w")
# file.write(name)
# file.close()
# Notice that the open function opens a file called names.txt with writing enabled, as signified by the w. The code above assigns that opened file to a variable called file. The line file.write(name) writes the name to the text file. The line after that closes the file.


# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close();



# ============= with ===============
# The keyword with allows you to automate the closing of a file.

# name = input("What's your name? ")
# with open("names.txt", 'a') as file:
#     file.write(f"{name}\n")
# Here we'r using the with so we don't need to close the file with will take care of it

# Up until this point, we have been exclusively writing to a file. What if we want to read from a file? To enable this functionality, modify your code as follows:

# with open("names.txt", 'r') as file:
#     lines = file.readlines()
    # Notice that readlines has a special ability to read all the lines of a file and store them in a list called lines. 
    
# for line in lines:
#     print("hello", line.rstrip()) 
    # Notice that "rstrip" has the effect of removing the extraneous line break at the end of each line.

# Still, this code could be simplified even further:
# with open("names.txt", 'r') as file:
#     for line in file:
#         print("hello,", line.rstrip())


# This code could be further improved to allow for the sorting of the names:

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
