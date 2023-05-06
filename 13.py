

#Problem-13: Write a program to implement a queue data 
# structure along with its typical operation.
class Queue:

    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to front element in the queue if present
        self.rear = -1  # rear points to last element in the queue
        self.count = 0  # current size of the queue

    # Function to remove front element from the queue
    def pop(self):
        # check for queue underflow
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating Program.")
            exit(1)

        print("Removing element : ", self.q[self.front])

        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    # Function to add a value to the queue
    def append(self, value):
        # check for queue overflow
        if self.isFull():
            print("OverFlow!! Terminating Program.")
            exit(1)

        print("Inserting element : ", value)

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    # Function to return front element in the queue
    def peek(self):
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating Program.")
            exit(1)

        return self.q[self.front]

    # Function to return the size of the queue
    def size(self):
        return self.count

    # Function to check if the queue is empty or not
    def isEmpty(self):
        return self.size() == 0

    # Function to check if the queue is full or not
    def isFull(self):
        return self.size() == self.capacity


if __name__ == '__main__':

    # create a queue of capacity 100
    q = Queue(100)
    while True:
        print("Press 0 then exit.")
        print("Press 1 then go to append.")
        print("Press 2 then go to pop.")
        print("Press 3 then go to check isEmpty?")
        n = int(input())
        if n==0:
            print("EXIT.")
            break;
        elif n==1:
            x = int(input("Enter the element : "))
            q.append(x)
        elif n==2:
            print("Queue size is", q.size())
            print("Front element is", q.peek())
            q.pop()
        elif n==3:
            if q.isEmpty():
                print("Queue is empty")
            else:
                print("Queue is not empty")
