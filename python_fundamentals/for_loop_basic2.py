#Biggie Size
def pos(arr):
    for x in range (len(arr)):
        if arr[x]>0:
            arr[x] = "big"
    return arr

#Count Positives
def countPos(arr):
    count = 0
    for i in range (len(arr)):
        if arr[i]>0:
            count +=1
    arr[len(arr)-1] = count
    return arr

#Sum Total
def sumTotal(arr):
    sum = 0
    for i in range (len(arr)):
        sum += arr[i]
    return sum

#Average
def average(arr):
    sum = 0
    for i in range (len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    return avg

#Length
def length(arr):
    return len(arr)

#Minimum
def min(arr):
    if len(arr)<1:
        return False
    x = arr[0]
    for i in range(len(arr)):
        if x>arr[i]:
            x = arr[i]
    return x

#Maximum
def max(arr):
    if len(arr)<1:
        return False
    x = arr[0]
    for i in range(len(arr)):
        if x<arr[i]:
            x = arr[i]
    return x

#Ultimate Analyze
def ultimate(x):
    L = {
        "total" : sumTotal(x),
        "average" : average(x),
        "maximum" : max(x),
        "minimum" : min(x),
        "length" : length(x)
    }
    for i in L:
        print (L[i])
      return L

print(ultimate([1,2,3,4]))

#Reverse List
def rev(arr):
    left=0
    right=len(arr)-1
    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right]=temp
        left += 1
        right -= 1
    # arr.reverse()
    return arr
arr = []
