# stack implementation on array

class Stack:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.top = -1
    
    def push(self, data):
        if self.top == self.capacity - 1:
            print("stack overflow")
            return
        else:
            self.top += 1
            self.arr[self.top] = data

    def pop(self):
        if self.top == -1:
            print("stack underflow")
            return
        else:
            popped = self.arr[self.top]
            self.top -= 1
            return popped
        
    def peek(self):
        if self.top == -1:
            print("stack is empty")
            return
        else:
            return self.arr[self.top]
    
    def is_empty(self):
        return self.top == -1
    
    def size(self):
        return self.top + 1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def display(self):
        if self.top == -1:
            print("stack is empty")
            return
        else:
            for i in range(self.top, -1, -1):
                print(self.arr[i], end=" ")
            print()
    
if __name__ == "__main__":
    S = Stack(5)
    S.push(10)
    S.push(20)
    S.push(30)
    print(S.pop())  # Output: 30
    print(S.peek()) # Output: 20
    S.display()     # Output: 20 10
    S.push(40)
    S.push(50)  
    S.is_empty() # Output: False
    S.is_full()  # Output: False
    S.push(60)
    S.push(70)    # Output: stack overflow