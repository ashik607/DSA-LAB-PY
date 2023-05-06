#Problem-3: Write a program to find an element
# using a linear search algorithm.
from array import *
def linearSeacrch(n,x,arr):
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return -1
#main function
n = int(input("Enter the number : "))
arr = array('i',[])
print("Enter the elements : ")
for i in range(0,n):
    m = int(input())
    arr.append(m)
while True:
    print("If press 1 then go to search.")
    print("If press 0 then exit.")
    press = int(input())
    if press==1:
        x = int(input("Enter the element number : "))
        ans = linearSeacrch(n, x, arr)
        if ans == -1:
            print(x, " are not present in this array")
        else:
            print(x, " are present in this ", ans, " number index array")
    else:
        print("Exit")
        break