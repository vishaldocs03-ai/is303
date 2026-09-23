# Declare the variable to store user's name, 
# destination, one-way distance in miles, vehicle MPG, gas price per gallon, 
# and number of travellers by getting input from user 

users_name = input("Enter your name here: ")
destination = input("Enter your destination here: ")
one_way_distance = float(input("Enter in miles the one way distance to your destination, please enter a number: "))
vehicle_mpg = float(input("Enter how many miles your vehicle gets per gallon of gas, please enter a number: "))
gas_price = float(input("Enter the cost of gas per gallon, please enter a number: "))
number_of_travellers = int(input("Enter how many people are taking the trip, please enter a whole number: "))

# Calculate total miles for the round-trip by doubling one_way_distance

round_trip_distance = one_way_distance * 2

# Calculate total gallons of gas needed for the round-trip by dividing round_trip_distance by vehicle_mpg

total_gallons_needed = round_trip_distance / vehicle_mpg

# Calculate total cost of gas for the round-trip by multiplying total_gallons_needed by gas_price

total_gas_cost = total_gallons_needed * gas_price

# Calculate cost per traveller by dividing total_gas_cost by number_of_travellers

cost_per_traveller = total_gas_cost / number_of_travellers

# Display the total cost for the trip and the cost per traveller by using the variables and their calculated values

print(f"{users_name} your trip to {destination} will cost a total of $  {total_gas_cost} for gas.")
print(f"The cost split evenly between {number_of_travellers} travellers is $ {cost_per_traveller} per person.")
