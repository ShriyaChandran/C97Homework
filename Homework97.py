import random
print("The number guessing game")
guessCount=0
number=random.randint(1,9)
introString=int(input("Enter a number from 1 to 9"))
while(guessCount<6):

    if(introString>number):
        print("The number is lesser than")
        print(introString)
        introString=int(input("Enter a number from 1 to 9"))
    elif(introString<number):
        print("The correct number is greater than ")
        print(introString)
        introString=int(input("Enter a number from 1 to 9"))
    else:
        print("Congratulations!! You guessed it man")
    guessCount=guessCount+1
if(guessCount==6):
    print("You lose. sad.")
