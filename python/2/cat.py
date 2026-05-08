# For Loops

for i in [0,1,2]:
    print("meow")
    
    

# Our code can be further improved. 

for i in range(3):
    print("meow")
    
# Notice how range(3) provides back three values (0, 1, and 2) automatically. This code will execute and produce the intended effect, meowing three times.




    
#  we never use it for any other purpose. In Python, if such a variable does not have any other significance in our code, we can simply represent this variable as a single underscore _. Therefore, you can modify your code as follows
for _ in range(3):
    print("meow")


# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")
    
    
# Bringing in our prior learning, we can use functions to further improve our code:

def main():
    meow(get_number())
    
def get_number():
    while True:
        n = int(input("what is n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")
        
        
main()        
