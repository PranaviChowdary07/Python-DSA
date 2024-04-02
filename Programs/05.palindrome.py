def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase
    s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
    
    for i in range(len(s) // 2):  # Iterate only through the first half of the string
        if s[i] != s[-i - 1]:  # Compare characters from both ends of the string
            return False
    return True

# Use a while loop to repeatedly  take from  user input
while True:
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The input string is a palindrome.")
    else:
        print("The input string is not a palindrome.")
