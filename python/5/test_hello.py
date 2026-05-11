# from hello import hello


# def test_hello():
#     assert hello("David") == "hello, David"
#     assert hello() == "hello, world"



# As with our previous test case in this lesson, we can break out our tests separately:

from hello import hello

def test_default():
    assert hello() == "hello, world"
    
def test_argument():
    assert hello("David") == "hello, David"
