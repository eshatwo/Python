import random
def randInt(max = 100, min = 0):
    x = int(random.random() * max)
    if x < min:
        x = x + min
    return(x)