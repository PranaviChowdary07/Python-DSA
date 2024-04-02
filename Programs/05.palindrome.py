def is_palindrome(s):
    s = s.replace(" ", "").lower()   # Remove spaces and convert to lowercase

    start = 0         # Initialize pointers for the beginning and end of the string
    end = len(s) - 1
    
    # Loop until the pointers meet
    while start < end:
       
        if s[start] != s[end]:
            return False    # If characters at the pointers don't match, return False
        start += 1
        end -= 1
    return True
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
