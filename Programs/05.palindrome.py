def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Initialize pointers for the beginning and end of the string
    start = 0
    end = len(s) - 1
    
    # Loop until the pointers meet
    while start < end:
        # If characters at the pointers don't match, return False
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

# Test the function
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
