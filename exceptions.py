def divideElements(lst, divider):
    try:
        return [i / divider for i in lst]
    except ZeroDivisionError as e:
        print(e)
        return lst

newlist = list(range(10))

""" Error if we divide by 0 """
divider= 0

print(divideElements(newlist, divider))