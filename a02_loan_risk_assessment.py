# Declare variables to store first name, last name, annual income, and monthly debt payments, 
# then set the value of the variables to the input given by the user

iFirstName = input("Enter your first name here: ")
iLastName = input("Enter your last name here: ")
fAnnualIncome = float(input("Enter your annual income in dollars: "))
fMonthlyDebt = float(input("Enter your monthly debt payments in dollars: "))

# debt to income income ratio calculation
# DTI = monthly debt / (annual income / 12)

fDTI = fMonthlyDebt/(fAnnualIncome/12)

# Round fDTI to two decimal places

fDTI = round(fDTI,2)

# Classify risk level based on calculated fDTI

if fDTI < 0.20:
    sRiskLevel = "Low Risk"
elif fDTI < 0.36:
    sRiskLevel = "Moderate Risk"
elif fDTI < 0.50:
    sRiskLevel = "Elevated Risk" 
else:
    sRiskLevel = "High Risk"

# Displaying results based on variables and their calcualted values 

print(f"{iFirstName} {iLastName} has a DTI of {fDTI}. The associated category is: {sRiskLevel}.")

