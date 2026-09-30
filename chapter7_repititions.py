#while loop 
sAnswer = "N"
sAnswer = input("Do you want to enter a student name?").upper()

while (sAnswer == "Y") :
    sFullName = input("Enter the student name: ")
    
    fGPA = float(input("Enter the " + sFullName + "'s GPA: "))
    
    print(sFullName, "has a GPA of", fGPA)
    
    sAnswer = input("Do you want to enter a student name?").upper()
    
print("Thank you")


    
