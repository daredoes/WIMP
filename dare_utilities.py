#Calculates Mode Values in a list
def mode(list = [], *args):
    top = 0
    mode_price = 0
    for p in list:
        if list.count(p) > top:

            top = list.count(p)
            mode_price = p
    return mode_price

#Calculates the Highest Value in a list
def high(list = [], *args):
    top = 0
    for p in list:
        if p > top:

            top = p
    return top

#Calculates the Lowest Value in a list
def low(list = [], *args):
    low = 10000000
    for p in list:
        if p < low:

            low = p
    return low