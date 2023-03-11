import random
import timeit

#Code for an efficient dequeue and inefficient enqueue and the corresponding testing code

class Node:
    def __init__(self, value, ranking):
        self.element = value
        self.priority = ranking
        self.next = None
    
    def getElement(self):
        return self.element
    def setElement(self, value):
        self.element = value
    def getPriority(self):
        return self.priority
    def setPriority(self, ranking):
        self.priority = ranking
    def getNext(self):
        return self.next
    def setNext(self, point):
        self.next = point

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def enqueue(self, data, importance):
        temp_node = Node(data, importance)
        if self.head == None:
            self.head = temp_node
            self.tail = temp_node
        else:
            current_node = self.head
            previous_node = None
            if importance < current_node.getPriority():
                temp_node.setNext(current_node)
                self.head = temp_node
            else:
                while current_node != None:
                    if current_node.getPriority() > importance:
                        temp_node.setNext(current_node)
                        previous_node.setNext(temp_node)
                        break
                    previous_node = current_node
                    current_node = current_node.getNext()
                if current_node == None:
                    previous_node.setNext(temp_node)
                    self.tail = temp_node


    def dequeue(self):
        dequeue_node = self.head
        if dequeue_node == None:
            return None
        if dequeue_node.getNext() == None:
            self.head = None
            self.tail = None
            return dequeue_node.getElement()
        else:
            self.head = dequeue_node.getNext()
            dequeue_node.setNext(None)
            return dequeue_node.getElement()    

# Generate a list of 1000 integers for testing
data = sorted(random.sample(range(1000), 1000))
priority_data = random.sample(range(1000), 1000)
queue_times = []
total_queue_times = 0

def test_dequeue_efficient(queue):
    i = 0
    while i < 1000:
        queue.dequeue()
        i = i + 1
dequeue_times = []
total_dequeue_times = 0
i = 0
queue_for_dequeue = PriorityQueue()
while i < 1000:
    queue_for_dequeue.enqueue(data[i], priority_data[i])
    i = i + 1

for i in range(100):
    dequeue_times.append(timeit.timeit(lambda: test_dequeue_efficient(queue_for_dequeue), number = 100))
    print(i)
for i in range(100):
    total_dequeue_times = total_dequeue_times + dequeue_times[i]
average_dequeue_time = total_dequeue_times / 100

print(f"Average time for dequeue efficient: {average_dequeue_time:.8f} seconds")

#function for testing enqueue
def test_enqueue_efficient(d, p):
    i = 0
    queue = PriorityQueue()
    while i < 1000:
        queue.enqueue(d[i], p[i])
        i = i + 1

#collects and displays the average time
for i in range(100):
    queue_times.append(timeit.timeit(lambda: test_enqueue_efficient(data, priority_data), number = 100))
    print(i)
for i in range(100):
    total_queue_times = total_queue_times + queue_times[i]
average_queue_time = total_queue_times / 100

print(f"Average time for enqueue inefficient: {average_queue_time:.8f} seconds")
