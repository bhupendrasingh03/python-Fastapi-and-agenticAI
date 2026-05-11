# from calculator import square


# def main():
#     test_square()


# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")


# if __name__ == "__main__":
#     main()


#  ================== assert ================== #
from calculator import square

# def main():
#     test_square()


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9


# if __name__ == "__main__":
#     main()
    
    
# One of the challenges that we are now facing is that our code could become even more burdensome if we wanted to provide more descriptive error output to our users. Plausibly, we could code as follows:



# def main():
#     test_squre()

# def test_squre():
#     try:
#         assert square(2) == 2
#     except AssertionError:
#         print("2 squared in not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared in not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared in not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared in not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared is not 0")
        
        
# if __name__ == "__main__":
#     main()
    
# Notice that running this code will produce multiple errors. However, it’s not producing all the errors above. This is a good illustration that it’s worth testing multiple cases such that you might catch situations where there are coding mistakes.

# The above code illustrates a major challenge: How could we make it easier to test your code without dozens of lines of code like the above?


# pytest is a third-party library that allows you to unit test your program. That is, you can test your functions within your program.
# To utilize pytest please type pip install pytest into your console window.
# Before applying pytest to our own program, modify your test_square function as follows:


# In the terminal window, type pytest test_calculator.py. You’ll immediately notice that output will be provided. Notice the red F near the top of the output, indicating that something in your code failed. Further, notice that the red E provides some hints about the errors in your calculator.py program. 
# Based upon the output, you can imagine a scenario where 3 * 3 has outputted 6 instead of 9. Based on the results of this test, we can go correct our calculator.py code as follows: => check the calculator.py

# def main():
#     test_square()


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0




# =========================
# To improve our test code, let’s modify test_calculator.py to divide the code into different groups of tests:

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) ==0