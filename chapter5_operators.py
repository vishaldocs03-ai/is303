# exponent operator 
calculation = 2 ** 8
print(calculation)

# modulo operator, only returns the remainder of a division
calculation_1 = 5 % 3
print(calculation_1)

# floor division operator, returns the only the quotient of a division, discarding the remainder, always rounds down
calculation_2 = 5 // 3
print(calculation_2)

# rounding
calculation_3 = round(5.6789, 2)
print(calculation_3)

# adding to the value of a variable
account_balance = 1000.00
account_balance = account_balance + 500.00
# this is the same as the line above
account_balance += 500.00
# this divides by 100
account_balance /= 100

#rounding
fnum1 = 4.5
print(f"{round(fnum1)}")
#print 4, uses bankers rounding, rounds 0.5 to the nearest even number
print( round(3.14159, 4) ) #rounds to four decimal
#rounding to the left of decimal
print( round(1897, -1)) #prints 1900, rounds to nearest tenth
print( round(1746, -2)) #print 1700, rounds to nearest hundreds
print( round(1456.95674, -3)) #print 1000, rounds to nearest thousands







