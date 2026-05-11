def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    # We can purposely break our calculator code by modifying it as follows:
    # return n * n 
    return n + n 



if __name__ == "__main__":
    main()