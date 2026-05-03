# Creating Our Own Parity Function
# As discussed in Lecture 0, you will find it useful to create a function of your own!
# We can create our own function to check whether a number is even or odd. Adjust your code as follows:

# x = int(input("What is x?"))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd");
    
def main():
    x = int(input("What is x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False
main();

# Notice that our if statement is_even(x) works even though there is no operator there. This is because our function returns a bool (Boolean), True or False, back to the main function. The if statement simply evaluates whether or not is_even of x is true or false.


# ================ We can further revise our code of def is_even(n)=============
def is_even(n):
    return True if n % 2 == 0 else False


# Even more 
def is_even(n):
    return n % 2 == 0

# Notice that the program will evaluate what is happening within the n % 2 == 0 as either True or False and simply return that to the main function.


