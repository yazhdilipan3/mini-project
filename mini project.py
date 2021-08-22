import random as r
import string

a = list(string.ascii_letters + string.digits)
b = ''
print(a)

for i in range(6):
    b+= r.choice(a)

print(b)
