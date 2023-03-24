def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max
