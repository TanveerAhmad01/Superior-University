import random

def fizz_buzz_game():
    print("Welcome to the Fizz Buzz game!")
    rounds = 5  
    for _ in range(rounds):
        number = random.randint(1, 100)  
        print(f"\nNumber: {number}")
        

        if number % 3 == 0 and number % 5 == 0:
            correct_answer = "Fizz Buzz"
        elif number % 3 == 0:
            correct_answer = "Fizz"
        elif number % 5 == 0:
            correct_answer = "Buzz"
        else:
            correct_answer = str(number)

    
        user_answer = input("Your answer (Fizz/Buzz/number): ").strip()
        
    
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}")

    print("\nGame over! Thanks for playing.")


fizz_buzz_game()
