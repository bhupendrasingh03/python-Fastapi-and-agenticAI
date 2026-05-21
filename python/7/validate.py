# Regular Expressions

# email = input("What's your email?").strip()

# if "@" in email:
#     print("Valid")
# else:
#     print("Invalid")
    
# We can be even more precise, modifying our code as follows:
# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

# Notice how the endswith method will check to see if domain contains .edu. Still, however, a nefarious user could still break our code. For example, a user could type in malan@.edu and it would be considered valid.

# Indeed, we could keep iterating upon this code ourselves. However, it turns out that Python has an existing library called re that has a number of built-in functions that can validate user inputs against patterns.
# One of the most versatile functions within the library re is search.
# The search function follows the signature re.search(pattern, string, flags=0). Following this signature, we can modify our code as follows:

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")