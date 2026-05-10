print("Hello", "world");

# x = int(input("What's x? "))
# print(f"x is {x}")

# Notice that by including the f, we tell Python to interpolate what is in the curly braces as the value of x. Further, testing out your code, you can imagine how one could easily type in a string or a character instead of a number. Even still, a user could type nothing at all – simply hitting the enter key.

# As programmers, we should be defensive to ensure that our users are entering what we expected.



# If we run this program and type “cat”, we’ll see ValueError: invalid literal for int() with base 10: 'cat'. In other words, the int function cannot convert the text “cat” into a number.

# An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.



# try:
#     x = int(input("What's x?"))
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")

# Notice how, running this code, inputting 50 will be accepted. However, typing in cat will produce an error visible to the user, instructing them why their input was not accepted.

# NameError where x is not defined

# ==============
# It turns out that there is another way to implement try that could catch errors of this nature.

# try:
#     x = int(input("What's x?"))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")




# ==================
# Considering improving our code, notice that we are being a bit rude to our user. If our user does not cooperate, we currently simply end our program. Consider how we can use a loop to prompt the user for x and if they don’t prompt again!
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")