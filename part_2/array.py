class MyArray:
    def __init__(self, capacity=10):
        self.data = [None] * capacity  # Fixed-size array
        self.size = 0

    def insert(self, index, value):
        if self.size >= len(self.data):
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise Exception("Invalid index")
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid index")

        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.size - 1] = None
        self.size -= 1

    def access(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid index")
        return self.data[index]

    def display(self):
        return self.data[:self.size]

# Example Usage
arr = MyArray(5)
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.delete(1)
print(arr.display())  # Output: [10, 30]