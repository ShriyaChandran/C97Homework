print("The number guessing game")
guessCount=0
number=random.randint(1,9)
introString=input("Enter a number from 1 to 9")
if(introString>number):
    print("The number is lesser than")
    print(number)
    introString=input("Enter a number from 1 to 9")
elif(introString<number):
    print("The correct number is greater than ")
    print(number)
    introString=input("Enter a number from 1 to 9")
else(introString==number):
    print:Congratulations!! You guessed it man
