def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1

    if k == 1:
        return n

    result = n
    idx = 1
    while idx != k:
        n -= 1
        result *= n
        idx += 1
    return result


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    n = 0
    while y >= 1:
        n += y % 10
        y = y // 10
    return n


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    previous_number = None
    while n >= 1:
        current_number = n % 10
        if (current_number == 8 and previous_number == current_number):
            return True
        previous_number = current_number
        n = n // 10
    return False


double_eights(2882)
