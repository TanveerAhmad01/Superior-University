class Punctuations:
    def __init__(self,str):
        self.str  = str
        self.list = ['.', ',', '?', '!', ':', ';', "'", '"', "'", '(', ')', '[', ']', '{', '}', '-', '–', '—', '...', '/', '\\', '|']

    def PrintChar(self):
        lis = []
        for char in self.str:
            if char in self.list:
                continue
            lis.append(char)
            my_string = ''.join(lis)
        print(my_string)



inp = input("Enter String: ")
obj = Punctuations(inp)
obj.PrintChar()
