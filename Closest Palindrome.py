#https://practice.geeksforgeeks.org/problems/closest-palindrome
# ///Given a number N. our task is to find the closest Palindrome number whose absolute difference with given number is minimum.
#
# Input:
# The first line of the input contains integer T denoting the number of test cases. Each test case contains a  number N.
#
# Output:
# For each test case, the print the closest palindrome number.
# Note:  If the difference of two closest palindromes numbers is equal then we print smaller number as output.
#
# Constraints:
# 1<=T<=1000
# 1<=n<=10^14


def getMiddle(n):
    if n % 2 == 0:
        return n // 2 - 1, n // 2
    else:
        return n // 2, n // 2

# Returns range of middle palindrome
def checkMiddle(array, n):
    if n % 2 == 0:
        i, j = n // 2 - 1, n // 2
    else:
        i, j = n // 2 - 1, n // 2 + 1

    while j < n and array[i] == array[j]:
        i -= 1
        j += 1
    return i , j

# Coppies left half of the array to right side
def copyL2R(array, low, high):
    while high < len(array):
        array[high] = array[low]
        high += 1
        low -= 1
    return array

# Adds 1 to middle digit, reccursive if value is 9
def addMiddle(array, i, j):
    if array[i] == 9:
        recurse = True
        array[i] = array[j] = 0
    else:
        recurse = False
        array[i] = array[j] = array[i] + 1

    if recurse:
        return addMiddle(array, i - 1, j + 1)
    else:
        return array

# Subtracts 1 from middle digit, reccursive if value is 0
def subMiddle(array, i, j):
    if array[i] == 0:
        recurse = True
        array[i] = array[j] = 9
    else:
        recurse = False
        array[i] = array[j] = array[i] - 1

    if recurse:
        return subMiddle(array, i - 1, j + 1)
    else:
        return array


# Program starts here
for i in range(int(input())):
    num = int(input())
    if num // 10 == 0:
        # Single digit, palindrome
        print(num)

    else:
        # Convert integer to int type list
        numList = list(map(int, str(num)))
        length = len(numList)
        low, high = checkMiddle(numList, length)
        if low == -1:
            # Number is palindrome
            print(num)

        else:
            leftSmall = False if numList[low] > numList[high] else True
            numList = copyL2R(numList, low, high)
            mid1, mid2 = getMiddle(length)
            if leftSmall:
                pLower = numList.copy()
                # Add one to middle to obtain higher palindrome
                pHigher = addMiddle(numList, mid1, mid2)
            else:
                pHigher = numList.copy()
                # Subtract one from middle to obtain higher palindrome
                pLower = subMiddle(numList, mid1, mid2)
            pLower = int(''.join(str(x) for x in pLower))
            pHigher = int(''.join(str(x) for x in pHigher))

            if num - pLower < pHigher - num:
                print(pLower)
            elif num - pLower > pHigher - num:
                print(pHigher)
            else:
                print(pLower)
