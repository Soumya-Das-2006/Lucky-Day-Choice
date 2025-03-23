import random
n = random.randint(1,100)
a = -1
gusse = 1
while(a!=n):
    a = int(input("Gusse A Number: "))
    if(a>n):
        print("Lower Number Please")
        gusse += 1
    elif(a<n):
        print("Higher Number Please")
        gusse += 1
print(f"You have guessed the number {n} correctly in {gusse} attemps")