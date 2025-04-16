def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_dict = {}
    text_l = text.lower()
    for character in text_l:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def get_sorted_character_list(character_dict):
    character_list = []

    for character, count in character_dict.items():
            if character.isalpha():
                 character_list.append({'char' : character, 'count' : count})
    def sort_on(dict):
         return dict["count"]
    character_list.sort(reverse=True, key=sort_on)
    return character_list
