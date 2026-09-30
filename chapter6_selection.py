#shorthand if statements
num1 = 7
num2 = 11
if ( num2 > num1 ):
    print(f"{num2} is greater than {num1}")

num3 = int(input("Please enter a whole number: "))
num4 = 4
if ( num3 % num4 == 0):
    print("Dividing", num3, "by", num4, "results in no remainder")
elif ( num3 % num4 != 0):
    print(f"{num3} is not divisible by {num4}, and thus results in a remainder")



if  ( num3 % num4 == 0 ) and (num3 > num4):  #both conditions need to be met 
    print("Both conditions are met!")

if ( num3 % num4 == 0 ) or (num3 > num4): #only one condition needs to be met
    print("One of the two conditions have been met!")


iOneA = 10
iTwoA = 20
iOneB = 10
iTwoB = 20

if ((iOneA, iTwoA) < (iOneB, iTwoB)) :
    print("Less than")
elif ((iOneA, iTwoA) == (iOneB, iTwoB)) :
    print("Equal to")
else :
    print("Greater than")

#nested if or else 
sDay = "M"
iNumber = 10

if (sDay.upper() == "M") :
    if (iNumber >= 0) and (iNumber <= 5) :
        print("Monday and 0 to 5")
    else :
        print("Monday and greater than 5")
else :
    if (iNumber >= 0) and (iNumber <= 5) :
        print("It is NOT Monday but the number is between 0 and 5")
    else :
        print("It is NOT Monday and the number is greater than 5") 








          
