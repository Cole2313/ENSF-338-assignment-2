import sys
import json
import time
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

def sort_and_time_array(arr):
    start_time = time.time()
    func1(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

def main(json_file):
    with open(json_file) as f:
        data = json.load(f)

    x = []
    y = []
    for array in data:
        size = len(array)
        x.append(size)
        time_taken = sort_and_time_array(array)
        y.append(time_taken)

    plt.plot(x, y)
    plt.xlabel("Size of Array")
    plt.ylabel("Time Taken (s)")
    plt.title("Time Taken vs Size of Array")
    plt.show()

if __name__ == "__main__":
    json_file = "ex2.json"
    main(json_file)