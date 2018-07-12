
def countdown(num):
    arr = []
    for i in range(num,-1,-1):
        arr.append(i)
    return arr


def printReturn(arr):
    if len(arr) != 2:
        return
    else:
        print(arr[0])
        return arr[-1]


def firstPlusLength(arr):
    if len(arr) == 0:
        return
    x = arr[0]+len(arr)
    return x


def valGreterSec(arr):
    newArr = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            newArr.append(arr[i])
            cnt += 1
    return newArr


def thisLenThatVal(x,y):
    if x == y:
        print("Jinx!")
    arr = []
    for i in range(x):
        arr.append(y)
    return arr
