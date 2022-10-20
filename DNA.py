#  File: DNA.py

#  Description: Locating the longest common subsequence between 2 DNA sequences

#  Student Name: Arnav Rai

#  Student UT EID: akr2673

#  Partner Name: Sashi Ayyalasomayajula

#  Partner UT EID: sa55465

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 8/27/22

#  Date Last Modified: 8/29/22

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

import sys


# returns a list of all substrings of a string
def all_substrings(s):
    # define a list to store all substrings
    result = []

    # define the length of the window
    wnd = len(s)

    # generate all substrings
    while (wnd > 0):
        idx = 0
        while (idx + wnd) <= len(s):
            sub_str = s[idx:idx + wnd]
            result.append(sub_str)
            idx += 1
        # decrease window size
        wnd = wnd - 1

    # return the result
    return result


# returns a list of all longest common substrings between s1 and s2
def longest_subsequence (s1, s2):
    longest_sub = []
    no_com_sub = ' '
    for subsequence in s1:
        for subsequence_2 in s2:

            if subsequence == subsequence_2:
                if len(subsequence_2) > len(longest_sub):
                    longest_sub.append(subsequence_2)

    for sub in longest_sub:
        if len(sub) < len(longest_sub[0]):
            longest_sub.remove(sub)

    if longest_sub:

        return longest_sub
    else:
        no_com_sub = 'No Common Sequence Found'
        return no_com_sub


# def test_cases():
    # test the function longest_subsequence
    assert longest_subsequence('a', 'a') == ['a']
    assert longest_subsequence('abcd', 'bc') == ['bc']
    assert longest_subsequence('abcd', 'xyz') == []
    assert longest_subsequence('', '') == []
    assert longest_subsequence('tsla', 'aapl') == ['a']
    assert longest_subsequence('unartistic', 'artists') == ['artist']

    # test the function all_substrings
    assert all_substrings('a') == ['a']
    assert all_substrings('') == []
    assert all_substrings('abc') == ['a', 'b', 'c', 'ab', 'bc', 'abc']

    # other test cases

    # return the result
    return 'All test cases passed'


def main():

    # call test_cases()
    # print(test_cases())
    # read the data
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)

    for x in range(num_pairs):

        s1 = sys.stdin.readline()
        s2 = sys.stdin.readline()
        s1 = s1.upper()
        s2 = s2.upper()
        s1 = s1.strip()
        s2 = s2.strip()
        # print(s1)
        # print(s2)
        s1_substrings = all_substrings(s1)
        s2_substrings = all_substrings(s2)
        # print(s1_substrings, s2_substrings)
        # longest_subsequence(s1, s2)
        longest_sub = longest_subsequence(s1_substrings, s2_substrings)

    # write out result(s)
        if type(longest_sub) == list:
            longest_sub.sort()
            for x in longest_sub:
                print(x)

        elif type(longest_sub) == str:
            print(longest_sub)

    # insert blank line
        print()


if __name__ == "__main__":

  main()




