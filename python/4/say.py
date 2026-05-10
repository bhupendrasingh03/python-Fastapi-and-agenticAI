# Packages
# One of the reasons Python is so popular is that there are numerous powerful third-party libraries that add functionality. We call these third-party libraries, implemented as a folder, “packages”.
# PyPI is a repository or directory of all available third-party packages currently available.
# cowsay is a well-known package that allows a cow to talk to the user.
# Python has a package manager called pip that allows you to install packages quickly onto your system.
# In the terminal window, you can install the cowsay package by typing pip install cowsay. After a bit of output, you can now go about using this package in your code.
# In your terminal window type code say.py. In the text editor, code as follows:

    
import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])


# Further modify your code:
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])