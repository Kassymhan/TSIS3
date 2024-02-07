import random
def func():
    s = 0
    print("Hello! What is your name?")
    name = input()
    print("Well,", name, "I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    n = int(input())

    a = random.randint(1, 20)
    while (a != n):
        if(a != n):
            if a < n:
                print("Your guess is too big.")
                print("Take a guess.")
                s += 1
            if a > n:
                print("Your guess is too low.")
                print("Take a guess.")
                s += 1
            
            n = int(input())
        
        if a == n:
            print("Good job, ", name, "You guessed my number in", s, "guesses!" )
            break

func()
    
            



