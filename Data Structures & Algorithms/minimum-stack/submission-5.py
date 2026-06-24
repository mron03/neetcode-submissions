class MinStack:

    def __init__(self):
        self.data = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        if not self.minimum:
            self.minimum.append(val)
        elif self.minimum[-1] >= val:
            self.minimum.append(val)
            

        self.data.append(val)

        print("Push : data:", self.data)
        print("Push : minimum:", self.minimum)
        

    def pop(self) -> None:
        if not self.data:
            return

        val = self.data.pop()

        if val == self.minimum[-1]:
            self.minimum.pop()

        print("Pop : data:", self.data)
        print("Pop : Minimum:", self.minimum)

        

    def top(self) -> int:
        if not self.data:
            return None
        
        return self.data[-1]

        

    def getMin(self) -> int:
        if not self.minimum:
            return None

        return self.minimum[-1]
        
