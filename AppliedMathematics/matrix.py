class matrix():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.elements = self.rows * self.columns

        self.data = []

    def add_data(self, data):
        if len(data) == self.elements:
            for i in range(0, self.rows, 1):
                self.data.append(list(data[i*self.columns : (i + 1) * self.columns]))
    
    def __repr__(self) -> str:
        return self.data

    def __sizeof__(self) -> int:
        return self.elements
    
    def __mul__(self, other):
        if type(other) == int:
            return str(self.data) + str(other)
        elif len(other.data) == len(other.data[0]):
            count = 0

            for row in self.data:
                for i in range(len(row)):
                    row[i] * other.data
                    
                


        
    def print_m(self):
        print(self.data)


#Testing
A = matrix(3,3)
A.add_data(["513874984", 123, 123, 123, 123, 123,123 ,123, "123"])

A.print_m()
print(A * 5)