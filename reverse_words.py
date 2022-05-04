def reverse_words(text):
    output_text_list = []
    splitted_text = text.split(' ')
    for word in splitted_text:
        output_text_list.append(word[::-1])
    output_text = ' '.join(output_text_list)
    return output_text


print(reverse_words('hello world again'))
