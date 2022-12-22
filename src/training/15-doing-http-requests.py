# Beware while testing your code:
# The checker don't have internet access, so you'll only get a:
#     "Temporary failure in name resolution"
# But you may run this on your computer.
import requests

try:
    r = requests.get('https://api.github.com/users/python')
    print(r.text)
except:
    print("No internet connectivity.")