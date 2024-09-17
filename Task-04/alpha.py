class Alpha:
    def __init__(self, input_str):
        self.stack = []
        self.input_str = input_str
       
    
    def convert(self):
        print(f"Orignal String: {self.input_str}")
        words = self.input_str.split()
        self.stack = words
        
       
    def bubblesort(self):
        n = len(self.stack)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.stack[j].lower() > self.stack[j+1].lower():
                    self.stack[j], self.stack[j+1] = self.stack[j+1], self.stack[j]
        print(f"Ordered String: {' '.join(self.stack)}")


usage = input("Write  text: ")
obj = Alpha(usage)
obj.convert()
obj.bubblesort()
