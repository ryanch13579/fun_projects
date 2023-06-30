import string

password = input('Password: ')

password_length = len(password)

with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print('Password was found in a common text file')
    print('Strength: Useless')
    exit()

def unique_upperchars(string):
    unique_char = set()

    for char in string:
        if char.isupper():
            unique_char.add(char)
    
    return len(unique_char)

def unique_lowerchars(string):
    unique_char = set()

    for char in string:
        if char.islower():
            unique_char.add(char)
    
    return len(unique_char)

def unique_digits(string):
    unique_char = set()

    for char in string:
        if char.isdigit():
            unique_char.add(char)
    
    return len(unique_char)

def unique_spec(string):
    unique_char = set()

    for char in string:
        if not char.isalnum():
            unique_char.add(char)
    
    return len(unique_char)

print(f'Uppercase letters: {unique_upperchars(password)}')
print(f'Lowercase letters: {unique_lowerchars(password)}')
print(f'Digits: {unique_digits(password)}')
print(f'Special Characters: {unique_spec(password)}')
print(f'Password length: {len(password)}')


u = unique_upperchars(password)
l = unique_lowerchars(password)
d = unique_digits(password)
s = unique_spec(password)

uscore = u - 1
lscore = l - 1
dscore = d - 1
sscore = s - 1

password_score = int((uscore + lscore + dscore + sscore)/password_length)

if password_length < 8:
    print('Password is weak')
    exit()

#check conditions
if u < 1 or l < 1 or d < 1 or s < 1:
    print('You are weak')
    exit()
elif u == 1 or l ==1 or d == 1 or s == 1:
    print('You can do better than that')
    exit()

print(f'Password score: {password_score}')





