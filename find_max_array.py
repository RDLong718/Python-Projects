# function finds the maxumber in an array
def find_max(array):
    """This is a function that finds the max number in an array.

    Args:
        array (list): list of numbers

    Returns:
        integer: a number
    """
    max = array[0]
    for i in array:
        if i > max:
            max = i
    return max


numbers = [1, 4, 7, 10, 20, 21, 19, 7, 3]
print(find_max(numbers))
