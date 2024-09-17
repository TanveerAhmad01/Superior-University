class visaCard:
    def __init__(self):
        self.visaCard = [5,5,9,0,4,9,0,2,1,5,9,0,0,7,1,1]
        self.lastNumber = ''

    def RemoveLastNubr(self):
        self.lastNumber= self.visaCard.pop()

    def Reverse(self):
        reverselist = []
        for i in self.visaCard[15::-1]:
            reverselist.append(i)
        self.visaCard = reverselist
        

    def EvenNumberDouble(self):
        emptylist = []
        for i in range(len(self.visaCard)):
            if i % 2 == 0:
                a = self.visaCard[i]
                b = a *2
                emptylist.append(b)
            else:
                a = self.visaCard[i]
                emptylist.append(a)
        self.visaCard = emptylist

    def substract(self):
        for i in self.visaCard:
            if i > 9:
                a = i -9
                self.visaCard.remove(i)
                self.visaCard.append(a)
        self.visaCard.append(self.lastNumber)

    def sum(self):
        a = 0
        for i in self.visaCard:
            a += i
        if a % 10 == 0:
            print("Valid Card")
        else:
            print("Not Valid Card")


obj = visaCard()
obj.RemoveLastNubr()
obj.Reverse()
obj.EvenNumberDouble()
obj.substract()
obj.sum()
