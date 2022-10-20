#  File: Triangle.py

#  Description: Finding the greatest sum path from a triangle of numbers with n numbers on each nth line, using different search methods.

#  Student Name: Arnav Rai

#  Student UT EID: akr2673

#  Partner Name: Tejas Bansal

#  Partner UT EID: tb34442

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/08/22

#  Date Last Modified: 10/10/22

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):

    sum_list = []
    def brute_helper(grid, total, row, col, fill):
        total += grid[row][col]
        if (row == len(grid) - 1):
            sum_list.append(total)

    return

# returns the greatest path sum using greedy approach
def greedy (grid):
    return

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    return

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    return

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)

    # create an empty grid with 0's
    grid = [[0 for i in range (n)] for j in range (n)]

    # read each line in the input file and add to the grid
    for i in range (n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list (map (int, row))
        for j in range (len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid

def main ():
    # read triangular grid from file
    grid = read_file()

    '''
    # check that the grid was read in properly
    print (grid)
    '''

    # output greatest path from exhaustive search
    times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
    times = times / 10
    # print time taken using exhaustive search

    # output greatest path from greedy approach
    times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
    times = times / 10
    # print time taken using greedy approach

    # output greatest path from divide-and-conquer approach
    times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
    times = times / 10
    # print time taken using divide-and-conquer approach

    # output greatest path from dynamic programming
    times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
    times = times / 10
    # print time taken using dynamic programming

if __name__ == "__main__":
    main()
