# Casey
# Mod gas gets user input based on menu choice Gas/G and returns to main

# Function gets user input for costPG, validates input and returns the
#   cost per gallon of gas
def get_costGas():
  costPG = 0.0
  while True:
    try:
      print("\nThe avg price per gallon in Portland is currently $3.974.")
      costPG = float(input("What do you pay per gallon? "))
      if costPG >= 5:
        print("That seems a little steep. Try again.")
        continue
    except ValueError:
      print("Please enter a cost between $0 and $5.")
      continue
    else:
      return costPG


# Function gets user input for vehicle's mpg, validates input and returns the
#   miles per gallon of said vehicle and returns mpg
def get_MPG():
  mpg = 0
  while True:
    try:
      print("\nAs of 2022, the most fuel effecient gas vehicle gets 61 mpg.")
      mpg = float(input("How many miles per gallon does your vehicle get? "))
      if mpg <= 8 or mpg > 62:
        print("Most vehicles average less than 62 mpg and more than 9mpg. \nPlease enter a number between 9 and 62.")
        continue
      return mpg
    except ValueError:
      print("Enter a valid mpg which should be between 9 and 61. \nUnless you're driving a tank or an electric bike.")
      continue
    else:
      return mpg

# Function calculates the cost of gas per mile based on user input above 
#   and returns cost_per_mile
def get_costPM(costPG, mpg):
  cost_per_mile = 0.0
  cost_per_mile = round((costPG / mpg),2)
  return cost_per_mile

