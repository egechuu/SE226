def reverse_string(s):
    return s[::-1]
def capitalize_words(s):
    return s.title()
def remove_punctuations(s):
    return s.replace('.', '').replace(',', '').replace(';', '').replace(':', '')

print(reverse_string("egeckc"))
print(remove_punctuations("asdfg.,dsfs,."))