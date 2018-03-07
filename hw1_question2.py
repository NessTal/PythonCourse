def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """

    result = []

    for i in list(range(100000,999996)):
        I = str(i)
        I = I[2:]
        if I == I[::-1]:
            I = str(i + 1)
            I = I[1:]
            if I == I[::-1]:
                I = str(i + 2)
                I = I[1:5]
                if I == I[::-1]:
                    I = str(i+3)
                    if I == I[::-1]:
                        result.append(i)

    return result


if __name__ == '__main__':
    # Question 2
    return_value = check_palindrome()

    print(f"Question 2 solution: {return_value}")
