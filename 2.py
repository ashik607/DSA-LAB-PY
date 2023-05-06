

#Problem-2: Write a program to sort a linear array using the bubble sort algorithm
from array import *

def bubbleSort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

#main function
while True:
    n = int(input("Enter the number : "))
    arr = array('i', [])
    print("Enter the array elements : ")
    for i in range(n):
        x = int(input())
        arr.append(x)

    bubbleSort(arr)
    print("After Bubble sorting : ")
    for i in range(0,len(arr)):
        print(arr[i], end=" ")
    print("\n")
