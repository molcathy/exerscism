def square(number):
    """
    The amount of grains of rice on a specific square
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """
    The total amount of grains of rice on the chessboard
    """
    return 2**64 - 1
