
#Problem-4: Write a program to find an element using the binary search algorithm
from array import *
def binrySearch(arr, n, x):
    lo=0
    hi=n-1
    while lo<=hi:
        mid = lo+(hi-1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            hi = mid-1
        else:
            lo = mid+1
    return -1
#main function
while True:
    n = int(input("Enter the number : "))
    arr1 = array('i',[])
    for i in range(0, n):
        x = int(input())
        arr1.append(x)
    r = int(input("Enter the search number : "))
    arr = sorted(arr1)
    result = binrySearch(arr, n, r)
    if result==-1:
        print("Element are not present in array.")
    else:
        print("Element are present at index ",result)