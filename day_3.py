"""
day 3
Each matrix on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few matrixs are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no matrixs are skipped), requested data must be carried back to matrix 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and matrix 1.

For example:

    Data from matrix 1 is carried 0 steps, since it's at the access port.
    Data from matrix 12 is carried 3 steps, such as: down, left, left.
    Data from matrix 23 is carried only 2 steps: up twice.
    Data from matrix 1024 must be carried 31 steps.

How many steps are required to carry the data from the matrix identified in your puzzle input all the way to the access port?
"""

x, y = 0, 0
n = 1
target = 277678

while True:
    if n == target:
        break
    x += 1
    n += 1
    x_dist = x
    if n == target:
        break
    while n != target and y < x_dist:
        y += 1
        n += 1
    if n == target:
        break
    while n != target and x > (0 - x_dist):
        x -= 1
        n += 1
    if n == target:
        break
    while n != target and y > (0 - x_dist):
        y -= 1
        n += 1
    if n == target:
        break
    while n != target and x < x_dist:
        x += 1
        n += 1
    if n == target:
        break
    while n != target and y < 0:
        y += 1
        n += 1
    if n == target:
        break

print(x, y)
print(abs(x) + abs(y))

"""
As a stress test on the system, the programs here clear the grid and then store the value 1 in matrix 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent matrixs, including diagonals.

So, the first few matrixs' values are chosen as follows:

    matrix 1 starts with the value 1.
    matrix 2 has only one adjacent filled matrix (with value 1), so it also stores 1.
    matrix 3 has both of the above matrixs as neighbors and stores the sum of their values, 2.
    matrix 4 has all three of the aforementioned matrixs as neighbors and stores the sum of their values, 4.
    matrix 5 only has the first and fourth matrixs as neighbors, so it gets the value 5.

Once a matrix is written, its value does not change. Therefore, the first few matrixs would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?
"""


x, y = 0, 0
n = 1
target = 277678
matrix = [[1, [0, 0]]]


def sum_adjacent(x, y):
    sum = 0
    for i, j in matrix:
        if j == [x + 1, y]:
            sum += i
            break
    for i, j in matrix:
        if j == [x - 1, y]:
            sum += i
            break
    for i, j in matrix:
        if j == [x, y + 1]:
            sum += i
            break
    for i, j in matrix:
        if j == [x, y - 1]:
            sum += i
            break
    for i, j in matrix:
        if j == [x + 1, y + 1]:
            sum += i
            break
    for i, j in matrix:
        if j == [x - 1, y + 1]:
            sum += i
            break
    for i, j in matrix:
        if j == [x + 1, y - 1]:
            sum += i
            break
    for i, j in matrix:
        if j == [x - 1, y - 1]:
            sum += i
            break
    return sum


while True:
    if n == target:
        break
    x_dist = x
    if n > target:
        break
    while n < target and y < x_dist:
        y += 1
        n = sum_adjacent(x, y)
        matrix.append([n, [x, y]])
    if n > target:
        break
    while n < target and x > (0 - x_dist):
        x -= 1
        n = sum_adjacent(x, y)
        matrix.append([n, [x, y]])
    if n > target:
        break
    while n < target and y > (0 - x_dist):
        y -= 1
        n = sum_adjacent(x, y)
        matrix.append([n, [x, y]])
    if n > target:
        break
    while n < target and x < x_dist + 1:
        x += 1
        n = sum_adjacent(x, y)
        matrix.append([n, [x, y]])
    if n > target:
        break

print(matrix)
