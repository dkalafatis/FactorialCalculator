def factorial(n):
    """Calculate the factorial of a positive integer n using recursion."""
    # Base case: if n is 0, the factorial is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


def main():
    try:
        # Prompt the user for an input
        num = int(input("Enter a positive integer: "))
        # Check if the input is negative; if so, prompt again
        if num < 0:
            print("Please enter a positive integer or zero.")
        else:
            # Calculate and print the factorial
            print(f"The factorial of {num} is {factorial(num)}.")
    except ValueError:
        # Handle the case where the input is not an integer
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
