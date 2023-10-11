#!/usr/bin/env python3


def minOperations(n):

    """
        Calculate the fewest number of operations needed to result
        in exactly n H characters in the file.

        :param n: The target number of H characters.
        :return: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
if __name__ == '__main__':
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
