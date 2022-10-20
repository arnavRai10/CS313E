#File: Intervals.py

#  Description: In this we read intervals.in and append all the tuples to a tuple list. From there we merge any tuples that have intersecting ranges. Finally we sort this updated list by the the difference between the first and second values of the tuples. Finally print both lists.

#  Student Name: Aayush Singh

#  Student UT EID: as92488

#  Partner Name: Danny Xie

#  Partner UT EID: dax56

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 1/29/2022

#  Date Last Modified: 1/31/2022
import sys
def read_input():
    num_of_intervals = int(input())
    tuples_list = []
    for i in range(num_of_intervals):
        line = input()
        line = line.split()
        tuples_list.append((int(line[0]),int(line[1])))

    return tuples_list

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the


def merge_tuples(tuples_list):
    final = []
    tuples_list.sort(key = lambda x: x[0])
    i = 0
    while i < len(tuples_list):
        right_val = tuples_list[i][1]
        j = i + 1
        while j < len(tuples_list):
            if tuples_list[j][0] <= right_val:
                right_val = max(right_val,tuples_list[j][1])
            else:
                final.append((tuples_list[i][0],right_val))
                break
            j = j+1
        if j == len(tuples_list):
            final.append((tuples_list[i][0],right_val))
        i = j

    tuples_list = final

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
    return tuples_list

def sort_by_interval_size (tuples_list):
    newList = []
    while tuples_list:
        minimum = tuples_list[0] #arbitrary num in list
        for x in tuples_list:
            if abs(x[1]-x[0]) < abs(minimum[0] - minimum[1]):
                minimum = x
            if abs(x[1]-x[0]) == abs(minimum[0] - minimum[1]):
                if x[0] < minimum[0]:
                    minimum = x
                if minimum[0] < x[0]:
                    continue
        newList.append(minimum)
        tuples_list.remove(minimum)

    return newList

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
  tuples_list = read_input()
  # merge the list of tuples
  tuples_list = merge_tuples(tuples_list)
  print(tuples_list)

  # sort the list of tuples according to the size of the interval
  tuples_list = sort_by_interval_size(tuples_list)
  print(tuples_list)

  # run your test cases
  #print (test_cases())

  # write the output list of tuples from the two functions

if __name__ == "__main__":
  main()
