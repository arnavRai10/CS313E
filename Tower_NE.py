import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    return peg4 (n, 1, 2, 3, 4)

def peg3 (n, source, dest, spare):
    # print(counter)
    if n == 1:
        # move the disc from source to dest
        return 1
    elif n == 0:
        return 0
    else:
        # counter += 1
        return 1 + peg3 (n - 1, source, spare, dest) + peg3 (n - 1, spare, dest, source)

def peg4 (n, source, dest, spare1, spare2):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        k = n - math.sqrt(2 * n + 1) + 1
        k = round(k)
        p = n-k-1

        return peg4 (k, 1, 2, 3, 4) + peg3 (p, 1, 3, 4) + 1 + peg3 (p, 3, 4, 1) + peg4 (k, 2, 4, 3, 1)

        

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()
