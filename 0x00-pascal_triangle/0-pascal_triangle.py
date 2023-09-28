#!/usr/bin/python3
'''
Create a function def pascal_triangle(n): that returns a list of lists of 
integers representing the Pascals triangle of n
''' 

def pascal_triangle(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    triangle = []

    for row_index in range(n):
        rowlist = []

        for i in range(row_index + 1):
            if i == 0 or i == row_index:
                rowlist.append(1)
            else:
                value = triangle[row_index - 1][i - 1] + triangle[row_index - 1][i]
                rowlist.append(value)

        triangle.append(rowlist)

    return triangle