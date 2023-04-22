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

    def print_m(self):
        print(self.data)


#Testing
A = matrix(3,3)
A.add_data(["513874984", 123, 123, 123, 123, 123,123 ,123, "123"])

A.print_m()
