# APIs

# APIs or “application program interfaces” allow you to connect to the code of others.
# requests is a package that allows your program to behave as a web browser would.



import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
