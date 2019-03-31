import threading
import time
import random

def calculateAverage1Thread():
    numbers = generateRandomNums(1000000)

    print("calculateAverage1Thread")

    thread = myThread("Thread 1", numbers)

    start = time.time()

    thread.start()
    thread.join()

    end = time.time()

    print("Averige is: " + str(thread.res))
    print("Duration: " + str(end - start) + " sec")

def calculateAverage4Thread():
    amount = 1000000
    numbers = generateRandomNums(amount)
    threads = []

    thread1 = myThread("Thread 1",numbers[:int(amount/2)])
    thread2 = myThread("Thread 2", numbers[int(amount/2):])

    threads.append(thread1)
    threads.append(thread2)

    print("calculateAverage4Thread")

    start = time.time()
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    sum = 0
    for i in range(0,len(threads)):
        sum += threads[i].res

    end = time.time()

    print("Averige is: " + str(sum / len(threads)))
    print("Duration: " + str(end - start) + " sec")

class myThread (threading.Thread):
    def __init__(self, name, data):
        threading.Thread.__init__(self)
        self.name = name
        self.data = data
        self.res = 0
        self.i = 0

    def run(self):
        self.res = calculateAverage(self.data)

def calculateAverage(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        sum += numbers[i]
    return sum/len(numbers)

def generateRandomNums(amount):
    numbers = list()
    for i in range(0,amount):
        numbers.append(random.randint(0,101))
    return numbers

if __name__ == '__main__':
    calculateAverage1Thread()
    calculateAverage4Thread()