

#Problem-5: Write a program to sort a linear array using the merge sort algorithm
from array import *
# Merge sort implementation
def mergeSorting(arr):
    if len(arr) > 1:
        # base case
        mid = len(arr) // 2
        lo = arr[:mid]
        hi = arr[mid:]
        mergeSorting(lo)
        mergeSorting(hi)
        i = j = k = 0
        while i < len(lo) and j < len(hi):
            if lo[i] < hi[j]:
                arr[k] = lo[i]
                i += 1
            else:
                arr[k] = hi[j]
                j += 1
            k += 1
        while i < len(lo):
            arr[k] = lo[i]
            i += 1
            k += 1
        while j < len(hi):
            arr[k] = hi[j]
            j += 1
            k += 1


#printing function
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

#main function
while True:
    n = int(input("Enter the number : "))
    arr = array('i', [])
    print("Enter the array elements : ")
    for i in range(0, n):
        x = int(input())
        arr.append(x)
    print("Given an array : ", end="\n")
    printList(arr)
    mergeSorting(arr)
    print("After sorted array : ", end="\n")
    printList(arr)