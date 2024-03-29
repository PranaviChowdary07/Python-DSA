def reverse_words(input_str):
    words = input_str.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words back into a string

# Example usage:
input_str = "pranavi learn python"
output_str = reverse_words(input_str)
print("Output:", output_str)
