get_text = input("Text: ")
LIST_OF_WORDS = {}
string_list = get_text.split(" ")
for current_word in string_list:
    if current_word not in LIST_OF_WORDS:
        LIST_OF_WORDS[current_word] = 0
    LIST_OF_WORDS[current_word] += 1
# print(LIST_OF_WORDS)
sorted_dictionary = dict(sorted(LIST_OF_WORDS.items()))
# print(sorted_dictionary)

longest_word = ""
for current_word in sorted_dictionary:
    if len(current_word) > len(longest_word):
        longest_word = current_word
longest_word_length = len(longest_word)

for current_line in sorted_dictionary:
    current_word, width, number = current_line, longest_word_length, sorted_dictionary[current_line]
    print(f"{current_line:{width}} : {number}")
    # print(current_line, ":", sorted_dictionary[current_line])
