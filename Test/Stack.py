class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, element):
        # ពិនិត្យមើលលក្ខខណ្ឌ Overflow
        if len(self.stack) >= self.size:
            print(f"Overflow! មិនអាចបន្ថែម {element} បានទេព្រោះ Stack ពេញ។")
        else:
            self.stack.append(element)
            print(f"Pushed: {element}")

    def pop(self):
        # ពិនិត្យមើលលក្ខខណ្ឌ Underflow
        if len(self.stack) == 0:
            print("Underflow! មិនអាច Pop បានទេព្រោះ Stack ទទេ។")
            return None
        else:
            removed = self.stack.pop()
            print(f"Popped: {removed}")
            return removed


# ដំណើរការសាកល្បង (កំណត់ទំហំត្រឹម 2)
my_stack = Stack(2)

# សាកល្បង Underflow
my_stack.pop()

# បន្ថែមទិន្នន័យ
my_stack.push("A")
my_stack.push("B")

# សាកល្បង Overflow
my_stack.push("C")
