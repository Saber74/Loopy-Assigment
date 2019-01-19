
import random
dice1=0
dice2=0
number=0 #for the total number of throws
totalDice=0
while totalDice!=2:
    dice1=int(random.randint(1,6))  #to generate a number between 1 and 6 #dice for the first dice throw
    dice2=int(random.randint(1,6))  #to generate a number between 1 and 6 for the second dice
    number=number+1
    totalDice=dice1+dice2 #to be able to get a certain value for the while loop total should be 2 and that's when we want it to stop for the eyes
    print(dice1,dice2)
print("It took %2.i throws to get snake eyes"%number)




 #question 2

population=36500000 #population of canada variable
years=0 # to see how many years it will take
while population<=100000000:
    population=population*1.14 #to continue adding the growth
    years=years+1
print("It took about %.2i years"%years)
#question 3

print("HEART ATTACKS ON A BUN".center(32,"-"))
print("1.The Big MOO Combo . . . 6.49\n2.BigMOO  . . . . . . . . 5.59\n3.Spring Surprise . . . . 2.49\n4.Fries . . . . . . . . . 1.59\n5.Pop . . . . . . . . . . 1.39\n6.Exit")
print("-"*32)
friesCounter=0 # to check if he ordered fires or not, if at 0 no fries were ordered
choice=0 # what they like to order from the list
total=0
# total money he has to pay
price=0
while choice!=6:
    choice=int(input("What would you like?: "))
    if choice==1:
        price=6.49
        friesCounter=friesCounter+1
    elif choice==2:
        price=5.59
    elif choice==3:
        price=2.49
    elif choice==4:
        friesCounter=friesCounter+1
        price=1.59
    elif choice==5:
        price=1.39
    elif choice==6:
        price=0 #to make sure the price value is reset upon exiting so it does not add it up again
        if friesCounter==0:#to ask if he wants fries or not
            ans=input("Do you like fries with that? :[y/n]: ").lower()
            if ans=="y":
                total=total+1.59 #not working

            
    else:
        print("Please try again")
    total=total+price
if total>3.99:
    total=total+total*0.13
print("Your total is $%.2f"%total)


#question4
balls=27000 #number of balls
levels=0 #number of levels
num=0 #number that will increase on each level
leftOver=27000 #how many left
total=0 #total number of balls used across all levels
while (levels+1)**2+total<27000: #to stop before actually reaching a number more than the number of balls we have
    levels=levels+1
    num=levels**2
    total=total+num
    leftOver=balls-total
    print(total,leftOver,levels)
    
print("%i ball will be used"%total+"\n%i balls will be leftover"%leftOver+"\npyramid is %i levels"%levels)


    



