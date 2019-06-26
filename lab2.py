import time
import random
import sys
from matplotlib import pyplot as plt
import numpy as np
import math

def generateData(kb):
    size = kb * 1024
    numbers = list()
    while sys.getsizeof(numbers) < size :
        numbers.append(0)
    return numbers

def calculateAverage(numbers, offset):
    sum = 0
    for i in range(0, len(numbers)):
        sum += numbers[i]
    print(offset)
    return sum/len(numbers)

def calculate(numbers, size, steps):
    for i in range(0, steps):
        a = (i*16) % len(numbers)
        numbers[a] += 1

def createHistogram(data):
    times = list()
    sizes = list()

    for d in data:
        times.append(d["time"])
        sizes.append(d["size"])

    plt.bar(np.arange(len(times)), times)
    plt.xticks(np.arange(len(times)), sizes)
    plt.xlabel('Velićina podataka u KB')
    plt.ylabel('Vrijeme u tikovima')
    plt.show()

def doWork():
    Size = 1
    times = list()

    for i in range(1,16):
        print("run: " + str(i))
        print("Generating data...")
        numbers = generateData(Size)
        print("Size of numbers: " + str(sys.getsizeof(numbers)/1024) + "in KB")
        print("Calculating...")
        start = time.perf_counter_ns()
        k=0
        #for k in range(0,(16-i)):
        calculate(numbers, Size, 2*1024*1024)
        #print(k)
        #calculateAverage(numbers, k)
        end = time.perf_counter_ns()
        size = Size
        times.append({"time":(end-start)/1000000000, "size":size})
        Size *= 2

    print(times)
    createHistogram(times)

if __name__ == '__main__':
    doWork()