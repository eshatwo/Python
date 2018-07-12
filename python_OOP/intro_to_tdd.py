import unittest

def reverseList(arr):
    for i in range(int(len(arr)/2)):
        hold = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = hold
    # arr.reverse()
    return arr

def isPalindrome(randStr):
    randStr = randStr.upper()
    for i in range(int(len(randStr)/2)):
        if randStr[i] != randStr[-1 -i]:
            return False
    return True

def coins(monies):
    d = {
        'q' : 25,
        'd' : 10,
        'n' : 5,
        'p' : 1,
        }
    totalCoins = []
    for i in d:
        count = int(monies / d[i])
        totalCoins.append(count)
        monies -= d[i] * count
    return totalCoins

if __name__ == "__main__":
    unittest.main()