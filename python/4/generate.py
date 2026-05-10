import random;
# coin = random.choice(["heads", "tails"]);
# print(coin);


# We can improve our code. from allows us to be very specific about what we’d like to import. Prior, our import line of code is bringing the entire contents of the functions of random. However, what if we want to only load a small part of a module? Modify your code as follows:

from random import choice
coin = choice(["heads", "tails"]);
print(coin)



# Moving on, consider the function random.randint(a, b). This function will generate a random number between a and b. Modify your code as follows:

number = random.randint(1, 10)
print(number);
# Notice that our code will randomly generate a number between 1 and 10.


# We can introduce the function random.shuffle(x), which shuffles a list into a random order.
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)
    
# Notice that random.shuffle will shuffle the cards in place. Unlike other functions, it will not return a value. Instead, it will take the cards list and shuffle them inside that list. Run your code a few times to see the code functioning.