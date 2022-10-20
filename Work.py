#  File: Work.py

#  Description:  Conduct binary and linear search based on lines of code written and productivity factor

#  Student Name: Arnav Rai

#  Student UT EID: akr2673

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/28/22

#  Date Last Modified: 9/29/22

import sys, time



def sum_of_series(v, k):
    # Total lines
    sum = 0
    num_of_coffee = 0
    # Minimum number of lines written before next cup of coffee
    term = v

    # While the lines written is greater than zero
    while term > 0:
        # Create new term, for new cup of coffee
        term = v // (k ** num_of_coffee)
        # Add lines written in past term to total lines
        sum += term
        # iterate the coffee cups
        num_of_coffee += 1

    return sum


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    # use linear search here
    # create array
    code_lines = []
    for val in range(1, n+1):
        code_lines.append(val)

    # search through each possible value
    max_val = 0
    for x in code_lines:
        # Use sum of series method to test total lines written by series
        if sum_of_series(x, k) >= n:
            return x

    return x


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    # use binary search here
    # create range of numbers
    high_val = n
    low_val = 0

    while high_val > low_val:

        # Finding the middle
        mid = (high_val + low_val) // 2

        # Testing the middle value using the sum of series method to find total lines
        mid_code_lines = sum_of_series(mid, k)

        # If the series sum for the middle value equals total lines
        if mid_code_lines == n:
            break
        # If the series sum for the middle value is LESS than total lines, meaning it's not in first half
        elif mid_code_lines < n:
            low_val = mid + 1
        # If the series sum for the middle value is GREATER than the total lines, meaning it's not in second half
        elif mid_code_lines > n:
            high_val = mid - 1

    # This checks if the low value is closer to the minimum number, v, or if the middle value is
    if 0 <= (sum_of_series(low_val, k) - n) < (mid_code_lines - n):
        mid = low_val
    # This checks if the high value is closer to the minimum number, v, or if the middle value is
    elif 0 <= (sum_of_series(high_val, k) - n) < (mid_code_lines - n) or (mid_code_lines < n):
        mid = high_val
    else:
        mid = mid

    return mid




    return 0 # placeholder

# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

  # The line above main is for grading purposes only.
  # DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
