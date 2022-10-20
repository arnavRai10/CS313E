#! /user/bin/python3

import sys

def main():
    
    # read number of input line
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)
    
    # create variable to store the sum
    sum = 0
    
    # read lines of input and process
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        num = int(line)
        
        x = num % 10
        a = num // 10
        sum += a ** x
        
    # print the sum
    print(sum)

if __name__ == '__main__':
    main()
