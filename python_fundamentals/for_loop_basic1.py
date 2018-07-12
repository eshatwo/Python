//Basic
for x in range(0,151):
    print(x)

//Multiples of Five
for y in range(5, 1000000):
    if y % 5 == 0:
        print(y)

//Counting, the Dojo Way
for x in range(1,101):
    if x % 10 == 0:
        print("Dojo")
    if x % 5 == 0:
        print("Coding")
    if x % 10 != 0 and x % 5 !=0:
        print(x)
    
//Whoa. That Suckers Huge
sum = 0
for x in range(0,500000):
    if x % 2 == 1:
        sum += x
    print(sum)

//Countdown by Fours
for x in reversed(range(1,2018)):
    if x % 4 == 0:
        print(x)

//Flexible Countdown







//Predict the following outcomes
list = [3,5,1,2]
for i in list:
    print(i)
3
5
1
2

list = [3,5,1,2]
for i in range(list):
    print(i)
range can only be used with two integers so this will not run

list = [3,5,1,2]
for i in range(len(list)):
    print(i)
0
1
2
3


def say_hi(name):
    print("hello," + name)
