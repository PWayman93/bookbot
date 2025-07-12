def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_list = {}
    lower_case = text.lower()
    characters = list(lower_case)
    for char in characters:
        if char in character_list:
            character_list[char] += 1
        else:
            character_list[char] = 1
    return character_list

def sorted_list(character_count):
    characters = list(character_count.items())
    sorted_characters = sorted(characters, key=lambda x: x[1], reverse=True)
    return sorted_characters
