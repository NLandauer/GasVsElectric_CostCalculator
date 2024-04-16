#******************************************************************************
# Author:         Noelle Landauer & Casey ******
# Lab:            Lab 4, CIS 133Y
# Date:           02.06.22
# Description:    Calculates how much it costs to drive and electric or
#                  gas vehicle based on gas/electricity costs and commute.
# Input:          vehicle - str, choice - str, e-rate - float, costPG - 
#                  float, mpg - float, oneway - float, trips - int
# Output:         vehicle - str, commute_wkcost - float, commute_yrcost - float
# Sources:        Lab 4 specifications
#                 ELectric car khw/mile data: 
#                  https://ecocostsavings.com/average-electric-car-kwh-per-mile
#                 PGE rates:  
#                  https://portlandgeneral.com/about/info/pricing-plans
#                 https://www.askpython.com/python/examples/exit-a-python-
#                   program
#                 Gas vehicle fuel efficiency stats:
#                  https://www.consumerreports.org/fuel-economy-efficiency/best-
#                  worst-fuel-economy-a3183445363/                  
#******************************************************************************


# Noelle
import gas, elec
import sys

#def main():
def main():
  # declare all variables
  oneway = 0.0
  commute_distance_week = 0.0
  vehicle = ''
  cost_permile = 0.0
  commute_wkcost = 0.0
  commute_yrcost = 0.0

# Display introductory message to program
  intro()
  
  # Get name of vehicle for table at end
  vehicle = vehicle_name()
  
  # Menu - choose between gas & electric 
  cost_permile = menu()  
  while cost_permile == -1:
    sys.exit("\nBye!")

 # Get commute distance   
  oneway = oneway_commute()
  commute_distance_week = weekly_commute(oneway)
  
 # Calculate weekly and yearly costs for commute 
  commute_wkcost, commute_yrcost = commute(cost_permile, commute_distance_week)

# Display results
  print("\nFor a", vehicle, ":")
  print("Your weekly commute will cost: $","{:.2f}".format(commute_wkcost))
  print("Annually, your commute will cost: $", "{:.2f}".format(commute_yrcost))
# End main()

# Casey
# Introduction to program
def intro():
  print("Let's compare the costs of driving a Gas or an Electric car.")
  print("First we will take some information about the vehicle.")
  print("Once we have that we will calculate the weekly and yearly expenses.")

# Noelle & Casey
# Menu for Gas, Electric or quit
def menu():
  while True:  
    choice = input("\nChoose a type of Vehicle. \nG for Gas, E for Electric or \npress any other key to Quit: ")
    choice = choice.upper()
    if choice == "G":
      costGas = gas.get_costGas()
      mpg = gas.get_MPG()
      cost_permile = gas.get_costPM(costGas, mpg) 
    elif choice== 'E':
      e_rate = elec.elec_rate()
      cost_permile = elec.elec_dollar_miles(e_rate)
    else:
      cost_permile = -1
    return cost_permile    
#  end menu

# Noelle
# Get one-way commute distance
def oneway_commute():
  oneway = 0.0
  while True:
    try:
      oneway = float(input("\nHow far is your communting distance, one way, in miles? "))
    except ValueError:
      print("Please enter a number.")
      continue
    else:
      return oneway

#Calculate weekly commute distance in miles       
def weekly_commute(oneway):
  trips = 0
  weekly_commute = 0.0
  while True:
    try:
      trips = int(input("\nHow many days per week do you have to go in to your workplace? "))
      if trips not in range(0,8):
        print("Please enter an integer between 0 and 7.")
        continue
    except ValueError:
      print("Please enter a whole number.")
      continue
    else:
      weekly_commute = oneway * trips * 2
      return weekly_commute

# Get name of vehicle (string)
def vehicle_name():
  vehicle = ''
  vehicle = input("\nWhat is the name of the vehicle? ")
  return vehicle

# Casey
# Get length of commute
def commute(cost_per_mile, commute_distance_week):
  WORK_WEEKS = 50
  commute_week = 0.0
  commute_year = 0.0
  commute_week = round((cost_per_mile * commute_distance_week),2)
  commute_year = round((commute_week * WORK_WEEKS),2)
  return commute_week, commute_year

main()