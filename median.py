"""Median calculator."""
def median(strs: list[int]):
    sortList = sorted(strs)
    length = len(sortList)
    if (length%2 == 0):
        listlength = int(len(sortList) / 2)
        return (sortList[listlength-1] + sortList[listlength]) / 2
    else:
        return sortList[round(length/2)]

"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


print(median(numbers))
