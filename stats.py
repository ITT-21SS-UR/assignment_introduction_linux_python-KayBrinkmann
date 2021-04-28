import math
import sys


# calculates mean from list of numbers
def get_mean(lst):
    mean = sum(lst) / len(lst)
    return mean


# calculates median from list of numbers
def get_median(lst):
    sortedlst = sorted(lst)
    print(sortedlst)
    length = len(lst)
    if length % 2 == 0:
        median = (sortedlst[int(length/2)-1] + sortedlst[int(length/2)])/2
    else:
        median = sortedlst[length//2]
    return median


# calculates standard deviation from list of numbers utilizing the get_mean function
def get_std(lst):
    mean = get_mean(lst)
    squarednums = []
    for number in lst:
        squarednums.append((number-mean)**2)
    std = math.sqrt(sum(squarednums))
    return std


numsList = []

# checks if arguments were given and reads text file if they weren't
# replaces "," with "." and appends given or read numbers to a list as float
if len(sys.argv) < 2:
    nums = open("numbers.txt", "r").read()
    for num in nums.split():
        if "," in num:
            num = float(num.replace(",", "."))
        else:
            num = float(num)
        numsList.append(num)
else:
    x = 1
    while x < len(sys.argv):
        num = sys.argv[x]
        if "," in num:
            num = float(num.replace(",", "."))
        else:
            num = float(num)
        numsList.append(num)
        x = x+1


print(numsList)

print("mean: ", get_mean(numsList))

print("median: ", get_median(numsList))

print("std: ", get_std(numsList))
