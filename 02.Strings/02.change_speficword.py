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

""" 
Output:
Enter a line of text: Pranavi learn python
Enter the word to replace: Pranavi
Enter the new word: Lavanya
Output: Lavanya learn python
 """


# another code already text exist
def replace_word(input_str, old_word, new_word):
    words = input_str.split()  # Split the string into words
    for i, word in enumerate(words):
        if word == old_word:
            words[i] = new_word   # Replace the old word with the new word
    return ' '.join(words)  # Join the modified words back into a string
input_str = "pranavi learn python" 
old_word = "learn"
new_word = "study"
output_str = replace_word(input_str, old_word, new_word)
print("Output:", output_str)


""" 
Output:

Output: pranavi study python
 """

