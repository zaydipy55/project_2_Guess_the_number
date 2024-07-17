import random
n = random.randint(1,50)
a =-1
guess =0
while(a!=n):
    a = int(input("Guess the number please: "))
    if(a>n):
        print("Lower Number Please: ")
        guess +=1
    else:
        print("Higher Number Please: ")
        guess +=1
        
print(f"You guessed it in {guess} attempts")

    