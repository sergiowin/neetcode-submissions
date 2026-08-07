class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        retValue = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1 
        return retValue

    def resize(self) -> None:
        newData = [None] * (self.capacity * 2)

        for i in range(self.size):
            newData[i] = self.data[i]

        self.data = newData
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity