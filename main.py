import random
import string
print("Welcome to Password Generator Console")
n=int(input("Enter the number of password digits: "))
password=""
chars=string.ascii_letters
chars+=string.digits
chars+=string.punctuation
for i in range(n):
    characters=random.choice(chars)
    password+=characters
print("Your Generated Password is: "+password)