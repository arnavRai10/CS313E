#  File: Spiral.py

#  Description:

#  Student Name: Arnav Rai

#  Student UT EID: akr2673

#  Partner Name: Kyle Hodowany

#  Partner UT EID: kwh677

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 8/31/2022

#  Date Last Modified: 9/2/2022

import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n


def CreateSpiral ( n ):
    if (n % 2 == 0):
        n += 1
    Up, Down, Right, Left = (0, -1), (0, 1), (1, 0), (-1, 0)
    turnRight = {Up: Right, Right: Down, Down: Left, Left: Up}
    x, y = n // 2, n // 2
    dx, dy = Up
    spiralMatrix = [[None] * n for _ in range(n)]
    count = 0
    while True:
        count += 1
        spiralMatrix[y][x] = count

        new_dx, new_dy = turnRight[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy

        if (0 <= new_x < n and 0 <= new_y < n and spiralMatrix[new_y][new_x] is None):
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:
            x, y = x + dx, y + dy
            if not (0 <= x < n and 0 <= y < n):
                return spiralMatrix

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0


def IndexLookup(spiral, value):
    for row in range(len(spiral)):
        for col in range(len(spiral)):
            if(spiral[row][col] == value):
                return [row, col]


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

# Function to get the sum of all neighbors
def SumAdjacentNumbers(spiral, row, col):

    # Create accumulating variable to store sum of adjacent numbers
    sum_value = 0

    # Loop through one row behind and one row in front of row of the chosen number
    for r in range(row - 1, row + 2):
        # Loop through one column behind and one column in front of column of the chosen number
        for c in range(col - 1, col + 2):
            # check r and c are in bounds.
            if inbounds(r, c, spiral):
                # If value is inbounds, add it to the accumulator
                sum_value += spiral[r][c]

    # In the above nested loop there is a point where r == row and
    # c == col, but we don't want to count current cell.
    # If current cell is counted, it is removed.
    if spiral[row][col]:
        sum_value -= spiral[row][col]

    # return accumulator variable
    return sum_value

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0


# Checks if the value of to cell in the spiral exists
def inbounds(r, c, spiral):

    # returns a boolean value based on conditions
    return 0 <= r < len(spiral) and 0 <= c < len(spiral[r])


def main():

    # Store the dimension of the spiral as a variable
    spiralDimension = int(sys.stdin.readline().strip())
    # Create the spiral and store an an array
    spiral = CreateSpiral(spiralDimension)

    # receive the first number after dimensions as a string
    line = sys.stdin.readline().strip()
    # Loop through file to receive and process all numbers
    while (len(line)> 0):

        # convert line into an integer for processing
        num = int(line)

        # Store row and column of chosen number as variable
        val_row, val_col = IndexLookup(spiral, num)

        # Call function to get sum of adjacent cells to chosen number
        sum_adj = SumAdjacentNumbers(spiral, val_row, val_col)
        print(sum_adj)
        # read next line
        line = sys.stdin.readline().strip()


if __name__ == "__main__":
  main()
