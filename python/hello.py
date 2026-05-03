# print("hello, world");
# input("What's your name? ");
# print("hello, Dev");



# name = input("What's your name? ").strip().title();
# Print the output
# print(f"hello, {name}")


# We can create our own function called hello as follows:
# def hello():
#     print("hello")
    
    
# name = input("What's your name? ");
# hello();

# print(name)

# We can further improve our code:
def hello(to):
    print(("hello, "+ to).title())
    
name = input("What's your name? ")
hello(name);




