# what is Python?

# Functions in Py?
Functions are verbs or actions that the computer or computer language will already know how to perform.
The print function knows

# Hello world in python
print("Hello, world");

# Take user input in py
input()

# Take user input with arg 
input("what's your name?")

# Variables 
A variable is just a container for a value within your own program.
name = input("What's your name? ")
print("hello, world")
Notice that this equal = sign in the middle of name = input("What's your name? ") has a special role in programming. This equal sign literally assigns what is on the right to what is on the left. Therefore, the value returned by input("What's your name? ") is assigned to name.


name = input("What's your name? ")
print("hello, name")

Further editing our code, you could type

name = input("What's your name? ")
print("hello,")
print(name)


The result in the terminal window would be

What's your name? Dev
hello
Dev

# Comments
Comments are a way for programmers to track what they are doing in their programs and even inform others about their intentions for a block of code. In short, they are notes for yourself and others who will see your code!

# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)

# Improved version 
Here print function printing the helle with name variable in single line

Ask the user for their name
name = input("What's your name? ")

Print hello and the inputted name
print("hello,", name)

# Strings and Parameters
A string, known as a str in Python, is a sequence of text.
Rewinding a bit in our code back to the following, there was a visual side effect of having the result appear on multiple lines:

# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)


We can modify our code as follows:

# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)

We can modify our code as follows:

# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)
By providing end="" we are overwriting the default value of end such that it never creates a new line after this first print statement. Providing the name as “David”, the output in the terminal window will be hello, David.

Parameters, therefore, are arguments that can be taken by a function.


# Formatting Strings
Probably the most elegant way to use strings would be as follows:

# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")

Notice the f in print(f"hello, ${name}"). This is a special inidicator for python to treate this string a special way, different than previous approches we have illustrated  in this lecture

# Remove whitespace
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")
Rerunning this program, regardless of how many spaces you type before or after the name, it will strip off all the whitespace.

# Using the title method, it would title case the user’s name:
Capitalize the first letter of each word
name = name.title()

# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()

# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")



# Integers or int
In Python, an integer is referred to as an int.
First, we can declare a few variables.

x = 1
y = 2

z = x + y

print(z)
Naturally, when we run python calculator.py we get the result in the terminal window of 3. We can make this more interactive using the input function.

x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
Running this program, we discover that the output is incorrect as 12. Why might this be?

Prior, we have seen how the + sign concatenates two strings. Because your input from your keyboard on your computer comes into the interpreter as text, it is treated as a string. We, therefore, need to convert this input from a string to an integer. We can do so as follows:

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

The result is now correct. The use of int(x) is called “casting,” where a value is temporarily changed from one type of variable (in this case, a string) to another (here, an integer).

We can further improve our program as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)



# Float Basics
# A floating point value is a real number that has a decimal point in it, such as 0.52.

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)
# This will allow your user to enter 1.2 and 3.4 to present a total of 4.6.
# Let’s imagine, however, that you want to round the total to the nearest integer. Looking at the Python documentation for round, you’ll see that the available arguments are round(number[, ndigits]). Those square brackets indicate that something optional can be specified by the programmer. Therefore, you could do round(n) to round a digit to its nearest integer. Alternatively, you could code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the result
print(z)
The output will be rounded to the nearest integer.



# Def
Wouldn’t it be nice to create our own functions?
Let’s bring back our final code of hello.py by typing code hello.py into the terminal window. Your starting code should look as follows:

def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)

# Returning Values
You can imagine many scenarios where you don’t just want a function to perform an action but also to return a value back to the main function. For example, rather than simply printing the calculation of x + y, you may want a function to return the value of this calculation back to another part of your program. This “passing back” of a value we call a return value.

def main():
    n = int(input("What's x? "))
    print("X squared is", square(n))
    
def square(n):
    return n * n

main();




# Pseudocode
Pseudocode is an informal, language-independent way of describing the steps of an algorithm using plain language mixed with programming-like structure.

Start
Ask user for name
If name is empty
    Show error message
Else
    Print greeting with name
End