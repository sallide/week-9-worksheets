import string
import random

source = string.ascii_letters + string.punctuation + string.digits

print(source)

pwd = random.choices(source,k=8)

print(pwd)

print("".join(pwd))
