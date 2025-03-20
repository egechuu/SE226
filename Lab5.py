import random
import string
import yaml

passwords = []
replacements = {}
chars = []


print('Choose 10 characters (lowercase only) and assign 3 replacement options each:')
for _ in range(5):
    print('Enter a lowercase character: ')
    char = input()
    chars.append(char)
    reps = []
    for i in range(3):
        print('Enter a replacement for', char, ':')
        char2 = input()
        reps.append(char2)
    replacements[char] = reps


#print(yaml.dump(replacements))

for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)


categorized_passwords = {"Strong": [], "Weak": []}

for password in passwords:
    count = 0
    for key in replacements.keys():
        if key in password:
            replacement = random.choice(replacements.get(key))
            password = password.replace(key, replacement)
            count += 1
    if count > 4:
        categorized_passwords["Strong"].append(password)
    else:
        categorized_passwords["Weak"].append(password)


for category, passwords_in_category in categorized_passwords.items():
    print(f"{category} Passwords:")
    for pwd in passwords_in_category:
        print(pwd)
