def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """

    iterations = len(word) - 5
    result = False

    for i in list(range(0, iterations)):
        if word[i:i+6:2] == word[i+1:i+6:2]:
            result = True

    return result

if __name__ == '__main__':
    # Question 1
    param1 = 'aabbcc'
    return_value = trifeca(word=param1)

    print(f"Question 1 solution: {return_value}")
