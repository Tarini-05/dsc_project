def sort_words_by_length(input_string):
    words = input_string.split()
    sorted_words = sorted(words, key=len)
    return ' '.join(sorted_words)
input_string = input("Enter a sentence: ")
output_string = sort_words_by_length(input_string)
print("Output:", output_string)
