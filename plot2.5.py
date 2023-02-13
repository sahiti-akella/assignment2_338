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
    sortarray = json.load(file)

with open("ex2.5.json", "r") as file2:
    mixarray = json.load(file2)

sortedtimes = []
for i in sortarray:
    time = timeit.timeit(lambda: func1(i, 0, len(i) - 1), number=1)
    sortedtimes.append(time)

mixedtimes = []
for i in mixarray:
    mixtime = timeit.timeit(lambda: func1(i, 0, len(i) - 1), number=1)
    mixedtimes.append(mixtime)

length = [len(i) for i in sortarray]

plt.plot(length, sortedtimes, label = "Sorted Array", color = "black")
plt.plot(length, mixedtimes, label = "Shuffled Array", color = "pink")
plt.xticks(length)
plt.xlabel("Value")
plt.ylabel("Time(s)")
plt.title ("Plot of Timing Data")
plt.legend(loc="best")
plt.show()



