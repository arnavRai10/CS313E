#  File: Intervals.py

#  Description: Read in a list of intervals and store them as tuples. Merge the intervals if they overalap and then sort
# given list of intervals by the size of the interval.

#  Student Name: Arnav Rai

#  Student UT EID: akr2673

#  Partner Name: Tejas Bansal

#  Partner UT EID: tb34442

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/5/2022

#  Date Last Modified: 9/9/2022
import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval


def merge_tuples (tuples_list):

    # Create a new copied list based on the parameter
    tuple_merge_list = tuples_list
    # iteration variable
    x = 0

    # Creates a while loop that runs as long as the next interval is LESS than the final tuple in the list.
    # Keeps inside index
    while x + 1 <= len(tuple_merge_list) - 1:
        # If the second number in interval x is greater than or equal to the first number in interval x + 1
        if tuple_merge_list[x][1] >= tuple_merge_list[x + 1][0]:
            # Check if the second number of interval x is greater than the second number in interval x + 1
            if tuple_merge_list[x][1] > tuple_merge_list[x + 1][1] :
                # Next interval in merged list is (first number of interval x, and second number of interval x)
                tuple_merge_list[x + 1] = (tuple_merge_list[x][0], tuple_merge_list[x][1])
            else:
                # Next interval in merged list is (first number of interval x, and second number of interval x + 1)
                tuple_merge_list[x + 1] = (tuple_merge_list[x][0], tuple_merge_list[x + 1][1])
            tuple_merge_list.remove(tuple_merge_list[x])
        else:
            # No overlap, iterate to next value
            x += 1

    return tuple_merge_list

    # Input: tuples_list is a list of tuples denoting intervals
    # Output: a list of tuples sorted by ascending order of the size of
    #         the interval
    #         if two intervals have the size then it will sort by the
    #         lower number in the interval


def sort_by_interval_size (tuples_list):

    # New list to return
    sorted_list = []
    # While there is still a value to check in tuples_list
    while tuples_list:
        # Start with the first interval as the minimum
        min_val = tuples_list[0] # arbitrary num in list
        # Swift through intervals
        for x in tuples_list:
            # If the space between interval x is less than the space between the minimum interval
            if abs(x[1]-x[0]) < abs(min_val[0] - min_val[1]):
                # Set the minimum interval to x
                min_val = x
            # If space between interval is EQUAL to space between minimum interval, and the x value is less than minimum
            if abs(x[1]-x[0]) == abs(min_val[0] - min_val[1]):
                if x[0] < min_val[0]:
                    min_val = x
                if min_val[0] < x[0]:
                    continue
        sorted_list.append(min_val)
        tuples_list.remove(min_val)

    return sorted_list


    # Input: no input
    # Output: a string denoting all test cases have passed
def test_cases ():

    assert merge_tuples([(1,2)]) == [(1,2)]
    # write your own test cases

    assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
    # write your own test cases

    return "all test cases passed"


def main():

    # open file intervals.in and read the data and create a list of tuples
    num_intervals = int(sys.stdin.readline())
    # Create blank list
    tuple_list = []
    # Swift through file and create interval pairs and append them to list
    for i in range(1, num_intervals + 1):
        line = sys.stdin.readline()
        line_list = line.split(' ')
        line_list[0], line_list[1] = int(line_list[0]), int(line_list[1])
        tuple_list.append((line_list[0], line_list[1]))

    tuple_list.sort()
    # merge the list of tuples
    tuple_list = merge_tuples(tuple_list)
    print(tuple_list)
    # sort the list of tuples according to the size of the interval

    tuple_list = sort_by_interval_size(tuple_list)

    print(tuple_list)
    # run your test cases
    '''
    print (test_cases())
    '''

    # write the output list of tuples from the two functions


if __name__ == "__main__":
  main()
