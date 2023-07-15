def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Prompt the user for input
num = int(input("Enter a number: "))

# Call the factorial function
result = factorial(num)

# Display the result
print("The factorial of", num, "is", result)
