def get_num_words(text):
    splitted_text = text.split()
    return f"Found {len(splitted_text)} total words"

def count_characters(text):
    count_letters = {}
    text = text.lower()
    for letter in text:
        if letter in count_letters:
            count_letters[letter] += 1
        elif letter.isalpha():
            count_letters[letter] = 1
        else:
            continue
    return count_letters

def sort_on(items):
    return items["num"]

def sort_letters(input_dict):
    print(type(input_dict))
    list = []
    for letter in input_dict:
        list.append({"char": letter, "num": input_dict[letter]})

    list.sort(reverse=True, key=sort_on)
    print(list)
    return list