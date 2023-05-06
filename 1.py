

#Problem-1: Write a Program to
# insert and delete an element into a linear array


# Open the input and output files for redirection
# sys.stdout = open('python/output.txt', 'w')
# sys.stdin = open('python/input.txt', 'r')
#insert the element

from array import *

#insert the element
def insertElements(arr):
    idx = int(input("Enter the index number : "))
    ele = int(input("Enter the element : "))
    arr.insert(idx, ele)
    print("After insertion the array : ")
    for i in range(0,len(arr)):
        print(arr[i], end=" ")
    print("\n")

#delete the element
def deleteElements(arr):
    pos = int(input("Enter the delete index number : "))
    arr.remove(arr[pos])
    print("After the delete the element : ")
    for i in range(0,len(arr)):
        print(arr[i], end=" ")

#main function
n = int(input("Enter the number : "))
arr = array('i', [])
print("Enter elements are : ")
for i in range(n):
    x = int(input())
    arr.append(x)
while True:
    print("\nIf press 1 then go to insert option.")
    print("If press 2 then go to delete option.")
    print("If press 0 then go to exit.")
    press = int(input())
    if press==1:
        insertElements(arr)
    elif press==2:
        deleteElements(arr)
    else:
        print("Exit")
        break
