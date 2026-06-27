from collections import deque


class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = deque()

    def enqueue(self, element):
        # ពិនិត្យមើលលក្ខខណ្ឌ Overflow
        if len(self.queue) >= self.size:
            print(f"Overflow! មិនអាចបញ្ចូល {element} បានទេព្រោះ Queue ពេញ។")
        else:
            self.queue.append(element)
            print(f"Enqueued: {element}")

    def dequeue(self):
        # ពិនិត្យមើលលក្ខខណ្ឌ Underflow
        if len(self.queue) == 0:
            print("Underflow! មិនអាច Dequeue បានទេព្រោះ Queue ទទេ។")
            return None
        else:
            removed = self.queue.popleft()  # យកចេញពីខាងមុខ
            print(f"Dequeued: {removed}")
            return removed


# ដំណើរការសាកល្បង (កំណត់ទំហំត្រឹម 2)
my_queue = Queue(2)

# សាកល្បង Underflow
my_queue.dequeue()

# បន្ថែមទិន្នន័យ
my_queue.enqueue("X")
my_queue.enqueue("Y")

# សាកល្បង Overflow
my_queue.enqueue("Z")
