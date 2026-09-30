#initialize list, initialize expense to store input, and set expense = 1 (any nonzero number) so that the loop starts
expense = 1
log_of_user_expenses = []
number_of_expenses = 0

#loop to keep asking for expenses unless user enters 0
while expense != 0:
    
    expense = float(input("Please enter an expense or 0 to finish: "))

    #check for negative user input, and prompt them to enter a positive amount
    if expense < 0:
         print("Invalid response, please enter a positive amount or 0 to exit: ")

    #if expense entered is positive and not 0, add to list and increment expense count by 1     
    elif expense > 0:
        log_of_user_expenses.append(expense)
        number_of_expenses += 1
        
#loop ends if user enters 0

#if user enters 0 as first value, exit program right away, if not continue with expense summary generation
if len(log_of_user_expenses) == 0:
     print("No expenses were entered.")
else:
    #initialize small_expenses, moderate_expenses, & large_expenses
    small_expenses = 0
    moderate_expenses = 0
    large_expenses = 0

    #loop through list and categorize expenses as small, moderate, or large
    for numbers in log_of_user_expenses:
            if numbers < 25:
                small_expenses +=1

            elif numbers >= 25 and numbers <= 100:
                moderate_expenses += 1

            elif numbers > 100:
                large_expenses += 1

    #initialize variables for avg_expense, smallest_expense, largest_expense, total_expenses and calc them using appropriate functions
    avg_expense = (sum(log_of_user_expenses)) / (len(log_of_user_expenses))
    smallest_expense = min(log_of_user_expenses)
    largest_expense = max(log_of_user_expenses)
    total_expenses = sum(log_of_user_expenses)


    #print output by calling variables
    print("Expense Summary")
    print("---------------")
    print(f"Number of expenses: {number_of_expenses}")
    print(f"Total: ${total_expenses:,.2f}")
    print(f"Average: ${avg_expense:,.2f}")
    print(f"Smallest expense: ${smallest_expense:,.2f}")
    print(f"Largest expense: ${largest_expense:,.2f}")
    print("")
    print(f"Small expenses: {small_expenses}")
    print(f"Moderate expenses: {moderate_expenses}")
    print(f"Large expenses: {large_expenses}")


random = 7