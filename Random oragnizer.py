import random
from random import shuffle

arr = [634 , 44, 345, 23, 567, 2, 765, 123543, 134 , 134, 44, 345, 23, 567, 2, 765, 123543, 134 , 134]

length = len(arr)

count = 0

peepee = True


def checkIfSorted(arr, count):
        
        num = 0
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                print(arr)
                return True
        print(arr)
        return False

while notSorted:
    notSorted = checkIfSorted(arr, count)
    count = count + 1

    shuffle(arr)

print(count)
