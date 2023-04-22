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
        elif self.columns == other.rows:
            count = 0
            res = []
            while (other.columns - count) != 0:
                sum = 0
                for row in self.data:
                    for i in range(self.columns):
                        sum += row[i] * other.data[i][other.columns - count - 1]
                res.append(sum)

                count += 1

            return res



        
    def print_m(self):
        print(self.data)

A = matrix(3,3)
A.add_data([1,2,3,4,5,6,7,8,9])
B = matrix(3,3)
B.add_data([2,2,2,2,2,2,2,2,2])
A.print_m()

#Testing
while True:
    exec(input(">>> "))