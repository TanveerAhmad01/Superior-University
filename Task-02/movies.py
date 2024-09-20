moviesDetils = [
    ("Eternal Sunshine of the Spotless Mind", 200),
    ("Memento", 90),
    ("Requiem for a Dream", 4500),
    ("Pirates of the Caribbean: On Stranger Tides", 3790),
    ("Avengers: Age of Ultron", 365),
    ("Avengers: Endgame", 3560),
    ("Incredibles 2", 20)
]

class movies:
    def __init__(self,MoviesName,Budeget):
        self.moviesName = MoviesName
        self.Budeget = Budeget
        
    def appendDataIntoList(self):
        data =(self.moviesName,self.Budeget)
        moviesDetils.append(data)
        print(moviesDetils)
    
    def AverageOfMovies(self):
        if not moviesDetils:
            print("No Movies to find Budget")

        for i in moviesDetils:
            CostOfMovies = i[1]

        totalMovies = len(moviesDetils)
        AverageBudgt = CostOfMovies/totalMovies
        print("Total Averge Of your Movies is: ",AverageBudgt)
        
    def OverBudget(self):
        total_out_of_budget = 0
        if len(moviesDetils) == 0:
            print("No movies To find")

        limitOfBudgt = int(input("Enter The Limit of Your Budget: "))
        for i in moviesDetils:
            moviesName = i[0]
            CostOfMovies = i[1]
            if CostOfMovies > limitOfBudgt:
                total_out_of_budget += 1
                print(f"{moviesName}: is out of Budget and heiger Budget Price is:",CostOfMovies - limitOfBudgt)
        print('====================================')
        print(f"Total: {total_out_of_budget} Movies is out of budget")

        

while True:
    choice = input("press -1 to add movies detils\npress -2 show over budget movies\npress -3 Average Budget\n")
    if choice == "1":
        movie = input("Enter Movies Name: ")
        budget = int(input("Enter Movies Budget: "))
        obj1 = movies(movie,budget)
        obj1.appendDataIntoList()
    
    elif choice == "2":
       
        obj3 = movies('','')
        obj3.OverBudget()

    elif choice == "3":
        obj2 = movies('','')
        obj2.AverageOfMovies()

