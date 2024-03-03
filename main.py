def main():
    with open("./books/Frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(word_count(file_contents))
        char_count_dictionary = character_count(file_contents)
        print(char_count_dictionary)
        character_report(char_count_dictionary)
        

def word_count(file_str):
    words = file_str.split()
    return len(words)

def character_count(file_str):
    character_dict = {}
    file_in_lower_case = file_str.lower()
    for char in file_in_lower_case:
        if char not in character_dict:
            character_dict[char] = 0
        character_dict[char] += 1
    return character_dict

def convert_flat_dictonary_to_list(dict):
    list = []
    for key in dict.keys():
        list.append({"char": key, "count": dict[key]})
    return list

def sort_on(dict):
    return dict["count"]

def character_report(char_dict):
    list = convert_flat_dictonary_to_list(char_dict)
    list.sort(reverse=True, key=sort_on)
    for item in list:
        print(f"The '{item["char"]}' character was found {item["count"]} times.")

main()