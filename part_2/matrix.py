class MyMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            raise Exception("Invalid index")
        self.data[row][col] = value

    def delete(self, row, col):
        if row >= self.rows or col >= self.cols:
            raise Exception("Invalid index")
        self.data[row][col] = 0

    def access(self, row, col):
        if row >= self.rows or col >= self.cols:
            raise Exception("Invalid index")
        return self.data[row][col]

    def display(self):
        for row in self.data:
            print(row)

# Example Usage
matrix = MyMatrix(3, 3)
matrix.insert(1, 1, 5)
matrix.display()