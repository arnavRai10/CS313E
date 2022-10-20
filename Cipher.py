#  File: Cipher.py

#  Description: Encrypts and decrypts strings

#  Student Name: Tejas Bansal

#  Student UT EID: tb34442

#  Partner Name: Arnav Rai

#  Partner UT EID: akr2673

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/11/22

#  Date Last Modified: 9/11/22

import sys

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt (strng):
    
    # find the smallest square number greater than or equal to the length of the given string
    l = len(strng)
    k = 0
    while(k < l):
        if(k**2 >= l):
            break
        else:
            k += 1

    # add asterisks if the square number is larger than the length of the string
    if(k ** 2 > l):
        while(k ** 2 > l):
            strng = strng + "*"
            l += 1
    
    # create the 2-D array with the square number of elements
    matrix = [[0 for x in range(k)] for y in range(k)]

    # populate the array with the original string
    counter = 0
    for i in range(k):
        for j in range(k):
            matrix[i][j] = strng[counter]
            counter += 1

    # read the encrypted version of the string
    tempStrng = ""
    for i in range(k):
        maxVert = k - 1
        for j in range(k):
            tempStrng = tempStrng + matrix[maxVert][i]
            maxVert -= 1
    
    # remove asterisks from encryption
    tempStrng = tempStrng.replace("*", "")
    
    return tempStrng


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt (strng):
    
    # find the smallest square number greater than or equal to the length of the given string
    l = len(strng)
    k = 0
    while(k < l):
        if(k**2 >= l):
            break
        else:
            k += 1
    
    # add asterisks if the square number is larger than the length of the string
    if(k ** 2 > l):
        while(k ** 2 > l):
            strng = strng + "*"
            l += 1
    
    # create the 2-D array with the square number of elements
    matrix = [[0 for x in range(k)] for y in range(k)]

    # populate the array with the original string
    counter = 0
    for i in range(k):
        for j in range(k):
            matrix[i][j] = strng[counter]
            counter += 1

    # read the encrypted version of the string
    tempStrng = ""
    maxHor = k - 1
    for i in range(k):
        for j in range(k):
            tempStrng = tempStrng + matrix[j][maxHor]
        maxHor -= 1
    
    # remove asterisks from encryption
    tempStrng = tempStrng.replace("*", "")
    
    return tempStrng

def main():
  # read the two strings P and Q from standard input
    p = sys.stdin.readline()
    p = p.strip()
    q = sys.stdin.readline()
    q = q.strip()
  
  # encrypt the string P
    encrypt(p)

  # decrypt the string Q
    decrypt(q)

  # print the encrypted string of P and the
  # decrypted string of Q to standard out
    print(encrypt(p))
    print(decrypt(q))
if __name__ == "__main__":
  main()