# Statistics
# Python comes with a built-in statistics library. How might we use this module?

# import statistics
# print(statistics.mean([100,90]))
# Notice that we imported a different library called statistics. The mean function takes a list of values. This will print the average of these values. In your terminal window, type python average.py.



# =================== Command-Line Arguments

# So far, we have been providing all values within the program that we have created. What if we wanted to be able to take input from the command-line? For example, rather than typing python average.py in the terminal, what if we wanted to be able to type python average.py 100 90 and be able to get the average between 100 and 90?

# "sys" is a module that allows us to take arguments at the command line.
# "argv" is a list within the sys module that records what the user typed on the command line.


import sys

# print("hello, my name is", sys.argv[1])
# Notice that the program is going to look at what the user typed in the command line. Currently, if you type python name.py David into the terminal window, you will see hello, my name is David. Notice that sys.argv[1] is where David is being stored. Why is that? Well, in prior lessons, you might remember that lists start at the 0th element. What do you think is held currently in sys.argv[0]? If you guessed name.py, you would be correct!


# try:
#     print("hello my bane is",sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# Our program can be improved as follows:


# if len(sys.argv) < 2:
#     print("Too far arguments")
# elif len(sys.argv) >2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])


# ============================= slice
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv:
#     print("hello, my name is", arg)

# Notice that if you type python name.py David Carter Rongxin into the terminal window, the interpreter will output not just the intended output of the names, but also hello, my name is name.py. How then could we ensure that the interpreter ignores the first element of the list where name.py is currently being stored?

# slice can be employed in our code to start the list somewhere different! Modify your code as follows:
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)
    
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# For avoiding twice print like if i type average.py Bp Singh => 
# i get
# "hello, my name is Bp"
# "hello, my name is Singh"
name = " ".join(sys.argv[1:])
print("hello, my name is", name)