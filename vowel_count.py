def get_count(sentence):
    count = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for letter in sentence:
        if letter in vowel_list:
            count += 1
    return count
