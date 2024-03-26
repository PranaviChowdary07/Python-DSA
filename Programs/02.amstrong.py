def is_armstrong_number(number):
    # Count number of digits
    num_length = len(str(number))
    # Initialize sum variable
    armstrong_sum = 0
    temp = number
    # Calculate Armstrong sum
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_length
        temp //= 10
       # Check if the sum is equal to the original number
    if armstrong_sum == number:
        return True
    else:
        return False
    # given input in code
""" number =145
ams = is_armstrong_number(number)
print("number",ams) """
# user takes input
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
