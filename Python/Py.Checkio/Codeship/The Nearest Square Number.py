from math import sqrt, floor


def nearest_square(number):
    number = sqrt(number)
    square = floor(number)
    return (square + 1) ** 2 if number - square > 0.5 else square ** 2


if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")
