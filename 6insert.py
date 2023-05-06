
# inset the link list

N = 16
info = [0]*100
link = [0]*100
start = -1
avail = -1
location = 0

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

def insert(item, loc):
    global start, avail
    if avail == -1:
        print("Overflow")
    newloc = avail
    avail = link[avail]
    info[newloc] = item
    if loc == 1:
        link[newloc] = start
        start = newloc
    else:
        pos = start
        while loc > 2:
            if info[link[pos]] == 0:
                break
            pos = link[pos]
            loc -= 1
        link[newloc] = link[pos]
        link[pos] = newloc

create_list(84, 5)
create_list(62, 12)
create_list(74, 7)
create_list(100, 8)
create_list(74, 13)
create_list(78, 6)
avail_list()

item, loc = map(int, input("Enter item and location: ").split())
insert(item, loc)
print("After inserting the list is:")
loc = start
while loc != 0:
    print(info[loc], end=" ")
    loc = link[loc]
