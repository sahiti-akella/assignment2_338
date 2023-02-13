import sys
import timeit
import json
import requests
import matplotlib.pyplot as plt

response = requests.get('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json', allow_redirects=True)
open('ex2.2.json', 'wb').write(response.content)

with open("ex2.2.json") as f:
    data = json.load(f)

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

length_data = []
timing_data = []


for i in data:
    time = timeit.timeit(lambda: func1(i, 0, len(i) - 1), number=1)
    length_data.append(len(i))
    timing_data.append(time)

plt.plot(length_data, timing_data)
plt.xlabel("Value")
plt.ylabel("Time(s)")
plt.title ("Plot of Timing Data")
plt.show()






