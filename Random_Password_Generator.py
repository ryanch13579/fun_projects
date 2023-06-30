import secrets, string

lower_letter = string.ascii_lowercase
upper_letter = string.ascii_uppercase
digits = string.digits
char = string.punctuation

lower_included = False
upper_included = False
digits_included = False
char_included = False
user_included = False

print()

print("** RANDOM PASSWORD GENERATOR **")

print()

length = int(input("Length of Password: "))

print()

characters = ''

print('Choose Password Composition:')

print()
print('Do you want to include uppercase letters?')
print(f'Example: {upper_letter[:5]}')
user_input = input('Y | N: ')
if user_input.lower() == 'y':
    characters += upper_letter
    upper_included = True
else:
    print('Please choose Y | N')
    print()
    exit()


print()
print('Do you want to include lowercase letters?')
print(f'Example: {lower_letter[:5]}')
user_input = input('Y | N: ')
if user_input.lower() == 'y':
    characters += lower_letter
    lower_included = True
else:
    print('Please choose Y | N')
    print()
    exit()

print()
print('Do you want to include digits?')
print(f'Example: {digits[:5]}')
user_input = input('Y | N: ')
if user_input.lower() == 'y':
    characters += digits
    digits_included = True
else:
    print('Please choose Y | N')
    print()
    exit()

print()
print('Do you want to include symbols?')
print(f'Example: {char[:5]}')
user_input = input('Y | N: ')
if user_input.lower() == 'y':
    characters += char
    char_included = True
else:
    print('Please choose Y | N')
    print()
    exit()

print()
print('Do you want to include custom characters?')
user_input = input('Y | N: ')
if user_input.lower() == 'y':
    user_char = input('Enter Custom Characters:')
    characters += user_char
    user_included = True

while True: 
    password = ''
    for n in range(length):
        character = secrets.choice(characters)
        password += character
    
    if lower_included and not any(c in lower_letter for c in password):
        continue

    elif upper_included and not any(c in upper_letter for c in password):
        continue

    elif digits_included and not any(c in digits for c in password):
        continue
    
    elif char_included and not any(c in char for c in password):
        continue

    elif user_included and not any(c in user_char for c in password):
        continue

    else:
        break

print()
print(f'Password: {password}')
print()
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


u = unique_upperchars(password)
l = unique_lowerchars(password)
d = unique_digits(password)
s = unique_spec(password)

uscore = u
lscore = l
dscore = d
sscore = s
password_length = len(password)

password_score =float( (uscore + lscore + dscore + sscore)/password_length)

if password_length < 8:
    print('Password is weak')
    exit()

#check conditions
if u < 1 or l < 1 or d < 1 or s < 1:
    print('You are weak')
    exit()

print(f'Password score: {format(password_score, ".2f")}')

if password_score < 0.25:
    print('Status: Weak')
elif password_score < 0.75:
    print('Status: Moderate')
elif password_score < 0.85:
    print('Status: Almost there')
else:
    print('Status: UnCrackable')

