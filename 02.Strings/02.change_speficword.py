def replace_word_in_line():
    input_str = input("Enter a line of text: ")  # Take input from the user
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")

    words = input_str.split()  # Split the string into words
    for i, word in enumerate(words):
        if word == old_word:
            words[i] = new_word  # Replace the old word with the new word

    output_str = ' '.join(words)  # Join the modified words back into a string
    print("Output:", output_str)
replace_word_in_line()


# another code already text exist
def replace_word_in_line():
    input_str = input("Enter a line of text: ")  # Take input from the user
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")

    words = input_str.split()  # Split the string into words
    for i, word in enumerate(words):
        if word == old_word:
            words[i] = new_word  # Replace the old word with the new word

    output_str = ' '.join(words)  # Join the modified words back into a string
    print("Output:", output_str)

# Call the function to replace the word in the line provided by the user
replace_word_in_line()

