import random
n = random.randint(1,100)
a = -1
guesses = 1

while(a != n):
    a =  int(input("Guess the number Please: "))
    if(a >n):
        print("Lower Number Please: ")
        guesses += 1
    elif(a<n):
        print("Higher Number Please: ")
        guesses += 1

print(f"You guessed the number {n} in {guesses} attempts!!!")

        