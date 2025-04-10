from string_package.manipulate import reverse_string, capitalize_words, remove_punctuations
from string_package.stats import count_characters, count_words, average_word_length

sentence = input("Enter a sentence: ")
if sentence != None:
    print("Reversed and capitalized: ", capitalize_words(reverse_string(sentence)))
    print("Removed punctuations: ", remove_punctuations(sentence))
    print("Character count: ", count_characters(sentence))
    print("Word count: ", count_words(sentence))
    print("Average word length: ", average_word_length(sentence))
