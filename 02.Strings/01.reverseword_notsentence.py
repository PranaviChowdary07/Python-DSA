def reverse_words(input_str):
    words = input_str.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reverse words. ' ' --> using for space in words
input_str = input("Enter the sentence:")
#input_str = "pranavi learn python"
output_str = reverse_words(input_str)
print("Output:", output_str)


# Output:
""" 
Enter the sentence:Pranavi learns Python
Output: ivanarP snrael nohtyP """