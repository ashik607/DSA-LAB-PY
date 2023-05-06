

#Problem-12: Write a program to solve
# the Tower of Hanoi problem for the 𝑁 disk.
def towerHanoi(n, A, B, C):
    if n==1:
        print("Move disc ",n," from ",A," to ",B)
        print(A, B, C)
    else:
        towerHanoi(n-1, A, C, B)
        print("Move disc ",n," from ",B," to ",A)
        print(A, B, C)
        towerHanoi(n-1, C, B, A)

while True:
    print("Press 1 then go to work.")
    print("Press 0 them exit.")
    n = int(input())
    if n==0:
        print("Exit.")
        break
    else:
        number = int(input("How many discs : "))
        a = 'A'
        b = 'B'
        c = 'C'
        print(a, b, c)
        towerHanoi(number, a, b, c)