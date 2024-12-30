import random
import string
def generate_password_complex(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password=""

    for i in range(length):
        password += random.choice(characters)
    return password
def generate_password_easy(length):
    characters = string.ascii_letters
    password=""

    for i in range(length):
        password += random.choice(characters)
    return password
def generate_password_medium(length):
    characters = string.ascii_letters + string.digits
    password=""

    for i in range(length):
        password += random.choice(characters)
    return password
print('_'*100,'\n')
print("Password Generator")
print('_'*100,'\n')

length=int(input("Enter the length of the required password:"))
if length<=0:
    print('_'*100,'\n')
    print("Password length should be greater than 0")
    print('_'*100,'\n')
    exit(0)
complexity=input("what complexity do you want?(simple,medium,complex):")
if complexity.lower()=="simple":
    print('_'*100,'\n')
    print("Password generated is: ",generate_password_easy(length))
if complexity.lower()=="medium":
    print('_'*100,'\n')
    print("Password generated is: ",generate_password_medium(length))
if complexity.lower()=="complex":
    print('_'*100,'\n')
    print("Password generated is: ",generate_password_complex(length))
print('_'*100,'\n')
print('_'*100,'\n')