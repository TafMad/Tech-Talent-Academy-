import random
print("Hello!What is your name?")
myName=input()
randomNumber=random.randint(1,10)
print("Well",myName,"I am thinking of a number between 1 and 10")
print("Take a guess of the number that i am thinking?")
guessNumber=int(input())
if guessNumber==randomNumber:
    print("Good job",myName,"!you guessed my number")
else:
   print("wrong ,better luck next time")