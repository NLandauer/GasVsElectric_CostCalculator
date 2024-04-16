#Noelle
# In elec module:
# Get electicity kWh rate from user
# Calculate $/mile for vehicle

# Declare average electric vehicle usage, unit kWh/100 miles
ELEC_CAR_USAGE = 35

# Get electricty rate, restricted to 0-0.5
def elec_rate():
  e_rate = 0.01
  print("\nWhat is the cost of your electricty per kWh?")
  print("\nIn Portland, PGE's Basic Service plan is $0.138 per kWh,")
  print("while the Green Future Choice plan is $0.146 per kWh.")
  while True:
    try:
      e_rate = float(input("Your rate per kWh: "))
      if e_rate <= 0 or e_rate > 0.5:
        print("Electricty costs are generally between $0 and $0.5 per kWh. Please re-enter.")
        continue
    except ValueError:
      print("Please enter a decimal between 0 and 0.5.")
      continue
    else:
      return e_rate

#calculate $/mile for electric vehicles
def elec_dollar_miles(e_rate):
  dollar_mile = round(((e_rate * ELEC_CAR_USAGE)/100),4)
  return dollar_mile







