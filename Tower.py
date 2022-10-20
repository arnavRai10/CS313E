#  File: Tower.py

#  Description: Tower of Brahma with 4 Needles

#  Student's Name: Arnav Rai

#  Student's UT EID: akr2673

#  Partner's Name: Tejas Bansal

#  Partner's UT EID: tb34442

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/13/22

#  Date Last Modified: 10/14/22

import sys, math

# Input: n the number of disks
# Output: returns the number of transfers using four needles


def num_moves (n):

  return fourth_peg(n, 1, 2, 3, 4)


def third_peg(n, source, dest, spare):
    # If there's only one disk remaining on the third peg
    if n == 1:
        # move the disc from source to dest
        return 1 # Counter of 1
    # If there's no pegs remaining on third peg, no move counted
    elif n == 0:
        return 0
    else:
        # 1 + represents counting a move, and recursion of third peg for the next ring on peg, and moving ring on spare to source
        return 1 + third_peg(n - 1, source, spare, dest) + third_peg(n - 1, spare, dest, source)

def fourth_peg(n, source, dest, spare_1, spare_2):
    # Same as third_peg
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        # Formula and solving for k
        k = n - ((2 * n + 1) ** (1/2)) + 1
        k = round(k)
        p = n - k - 1

        # Run 4th peg as normal recursion, with counts for moves on third peg and next ring on third peg and then again on 4th
        return fourth_peg(k, 1, 2, 3, 4) + third_peg(p, 1, 3, 4) + 1 + third_peg(p, 3, 4, 1) + fourth_peg(k, 2, 4, 3, 1)


def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int(line)
    print(num_moves(num_disks))

if __name__ == "__main__":
  main()
