# sort.py

import numpy
import time
import sys

# Quick Sort
# reference: https://www.youtube.com/watch?v=9KBwdDEwal8
def arraySwap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def hoarePartition(a, l, r):
    # p is pivot
    p = a[l]
    # i is left position after pivot
    i = l + 1
    # j is right position
    j = r
    # while i and j have not crossed
    while i < j:
        # scanning from left
        while i < r and a[i] < p:
            i = i + 1
        # scanning from right
        while j > l and a[j] > p:
            j = j - 1
        # if i and j have not crossed
        if i < j:
            arraySwap(a, i, j)
    # if i and j have crossed
    if a[j] < p:
        # swap the pivot with j
        arraySwap(a, l, j)
    # returns the split point
    return j
        
def quickSort(a, l, r):
    # if the array is not of size 1
    if l < r:
        # partitions the array and returns split point
        sp = hoarePartition(a, l, r)
        # recursively sort left subarray
        quickSort(a, l, sp - 1)
        # recursively sort right subarray
        quickSort(a, sp + 1, r)


# Selection Sort
def selectionSort(a):
    # for each element in the array
    for i in range(len(a) - 1):
        # set min element
        min = i
        # loop over the rest of the array
        for j in range(i + 1, len(a)):
            # if a new min is found
            if a[j] < a[min]:
                # set new min
                min = j
        # swap min element to correct position
        arraySwap(a, i, min)


# Insertion Sort
def insertionSort(a):
    # for each element in the array
    for i in range(1, len(a)):
        # v is element to sort
        v = a[i]
        j = i - 1
        # loops until it find viable position for v
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = v

# Main driver
def main():
    # opens output file
    sys.stdout = open ("output.txt", "w")

    # initilizes arrays
    array_sizes = [1000, 5000, 10000, 20000]
    arrays = []
    for size in array_sizes:
        arrays.append(numpy.random.rand(size))

    # sorts the arrays via Quick sort
    for array in arrays:
        array_copy = numpy.copy(array)
        start = time.time()
        quickSort(array_copy, 0, len(array) - 1)
        end = time.time()
        run_time = end - start
        print("Quick Sort Size ", len(array), " time: ", run_time)

    # sorts the arrays via Selection sort
    for array in arrays:
        array_copy = numpy.copy(array)
        start = time.time()
        selectionSort(array_copy)
        end = time.time()
        run_time = end - start
        print("Selection Sort Size ", len(array), " time: ", run_time)

    # sorts the arrays via Insertion sort
    for array in arrays:
        array_copy = numpy.copy(array)
        start = time.time()
        insertionSort(array_copy)
        end = time.time()
        run_time = end - start
        print("Insertion Sort Size ", len(array), " time: ", run_time)
    

    sys.stdout.close()
if __name__ == "__main__":
    main()