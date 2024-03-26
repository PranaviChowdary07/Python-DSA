def reverse_string(input_string):
    # empty string to store the reversed string
    reversed_string = ""
    
    # Iterate through the characters of the input string in reverse order
    for char in input_string[::-1]:
        
        reversed_string += char   
    return reversed_string

# Example usage:
input_str = input("Enter a string: ")
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)
