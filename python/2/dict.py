# Dictionaries
# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

# print(students);

# Notice that we can promise that we will always keep these lists in order. The individual at the first position of students is associated with the house at the first position of the houses list, and so on. However, this can become quite cumbersome as our lists grow!

# We can better our code using a dict as follows:
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# print(students["Hermione"])

# Notice how we use {} curly braces to create a dictionary. Where lists use numbers to iterate through the list, dicts allow us to use words.

# By running this code we will get the this o/p  => Gryffindor

# We can improve our code as follows:

# for student in students:
#     print(student, ':' ,students[student])



# What if we have more information about our students? How could we associate more data with each of the students?

# students = [
#     {"name":"Hermione", "house": "Gryffindor, Gryffindor1", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=" : " )


# Mario

# Remember that the classic game Mario has a hero jumping over bricks. Let’s create a textual representation of this game.
# https://cs50.harvard.edu/python/notes/2/cs50pWeek2Slide21.png
# Begin coding as follows:

# print("#")
# print("#")
# print("#")
# Notice how we are copying and pasting the same code over and over again.

# Consider how we could better the code as follows:

# for _ in range(3):
#     print("#")



# Consider: Could we further abstract for solving more sophisticated problems later with this code? Modify your code as follows:
# def main():
#     print_column(3)
    
# def print_column(height):
#     for _ in range(height):
#         print("#")
        
# main()


# def main():
#     print_square(3)


# def print_square(size):

#     # For each row in square
#     for i in range(size):
#         # For each brick in row
#         for j in range(size):
#             #  Print brick
#             print("#", end="")
#         # Print blank line
#         print()

# main()

# Notice that we have an outer loop that addresses each row in the square. Then, we have an inner loop that prints a brick in each row. Finally, we have a print statement that prints a blank line.

# We can further abstract away our code:

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()