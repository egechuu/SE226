def count_characters(s):
    return len(s)

def count_words(s):
    ls = s.split(' ')
    return len(ls)

def average_word_length(s):
    count = count_words(s)
    ls = s.split(' ')
    sum = 0
    for i in ls:
        sum += count_characters(i)

    return sum/count


print(average_word_length("sad dsa dad sa"))