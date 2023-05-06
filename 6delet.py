
#   delete in link list

N = 16
info = [0] * 100
link = [0] * 100
start = -1
avail = -1
location = None

def create_list(val, loc):
    global start, location
    if start == -1:
        start = location = loc
        info[start] = val
    else:
        info[loc] = val
        link[location] = loc
        location = loc

def avail_list():
    global avail, location
    for i in range(1, N+1):
        if info[i] == 0:
            if avail == -1:
                avail = location = i
            else:
                link[location] = i
                location = i

def Delete(loc):
    global start, avail
    if loc == 1:
        info[start] = 0
        temp = start
        start = link[start]
        link[temp] = avail
        avail = temp
        return
    preLoc = start
    while loc > 2:
        if info[link[preLoc]] == 0:
            break
        preLoc = link[preLoc]
        loc -= 1
    loc = link[preLoc]
    link[preLoc] = link[loc]
    info[loc] = 0
    link[loc] = avail
    avail = loc

# Test
create_list(84, 5)
create_list(62, 12)
create_list(74, 7)
create_list(100, 8)
create_list(74, 13)
create_list(78, 6)
avail_list()

loc = int(input("Enter location: "))
Delete(loc)
print("After deleting the node, the list is:")
loc = start
while loc != 0:
    print(info[loc], end=' ')
    loc = link[loc]
print()
