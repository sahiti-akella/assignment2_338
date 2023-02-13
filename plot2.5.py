import sys
import timeit
import json
import requests
import matplotlib.pyplot as plt


sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.2.json", "r") as file:
    array = json.load(file)

with open("ex2.5.json", "r") as file2:
    altarray = json.load(file2)


times = []
for i in array:
    time = timeit.timeit(lambda: func1(i, 0, len(i) - 1), number=1)
    times.append(time)

alttimes = []
for i in altarray:
    alttime = timeit.timeit(lambda: func1(i, 0, len(i) - 1), number=1)
    alttimes.append(alttime)

length = [len(i) for i in array]

plt.plot(length, times, label = "Sorted Array", color = "black")
plt.plot(length, alttimes, label = "Shuffled Array", color = "pink")
plt.xticks(length)
plt.xlabel("Value")
plt.ylabel("Time(s)")
plt.title ("Plot of Timing Data")
plt.legend(loc="best")
plt.show()



