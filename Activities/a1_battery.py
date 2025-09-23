"""
Battery Modeling Tutorial - Loops and Conditionals
This file demonstrates Python loops and conditional statements through 
a practical battery charging/discharging simulation over 10 time periods.

Learning objectives:
- Using for loops 
- Working with conditional statements (if/elif/else)
- List indexing and manipulation
- Variable assignment and updates

Complete the script by filling in the missing code sections marked with <---.
1) Ignore any battery constraints e.g. max/min state of charge, max power, efficiency, degradation etc
2) Revisit your completed code from (1) and add battery constraints. 
        You could do this by adding more nested if statements, or using min/max functions when calculating battery power.

This is a comment block or docstring which can span multiple lines. 
It is often used at the start of files to describe the file.
@author: PLACE YOUR NAME HERE
"""

# Import any necessary libraries 
import math

# Initialize battery parameters and variables
dt = 1  # Time step in hours
max_soc = 10  # Maximum state of charge (kWh)
min_soc = 1   # Minimum state of charge (kWh)
max_power = 15 # Maximum power the battery can handle (kW)
bat_eff = 0.98    # Base battery efficiency
bat_deg = 0.01    # Battery degradation factor
soc_0 = 5  # Initial state of charge (kWh)

# Create the demand variable (this represents energy demand over 10 periods)
# Positive values indicate demand is needed from the battery
# Negative values indicate excess energy that can be used to charge the battery
demand_P = [5, -8, 12, -3, 7, -10, 15, -5, 8, -2]


# Initialize lists to store battery power and state of charge
bat_P = [0] * len(demand_P)  # List to store battery power for each period, initialized to 0
soc =   # <--- List to store state of charge, starting at 50 kWh

# write code with the general structure:
# for loop:
#    if demand is positive:
#        discharge battery
#    else if demand is negative:
#        charge battery
#    else:
#        do nothing

# iterate through each time period using the range() function
for : # <--- Fill in the for loop to iterate over the range of demand_P length
    
    # Conditional logic - check if demand is positive or negative
    if demand_P[i] 0: # <--- Complete the condition to check if demand is positive
        # Case (a): Positive demand means discharge the battery
        
        # Calculate battery power (discharge = positive battery power)
        bat_P[i] = demand_P[i]
        
        # update state of charge (discharging reduces SoC)
        if i == 0:
            # first period uses initial SoC
            soc[0] = soc_0 - (bat_P[i] * dt
        else:
            # subsequent periods use previous timestamps SoC
            soc[i] = # <--- Update SoC when i > 0
        
    el # <--- complete the else if condition to check if demand is negative:
        # Case (b): Negative demand means charge the battery  
        
        # Calculate battery power (charging = negative power, its already negative)
        bat_P[i] = demand_P[i]
        
        # update state of charge (charging increases SoC)
        # <--- update SoC when i == 0 and i > 0. Think about the correct sign.

    else:
        # Case (c): Zero demand means no battery operation
        bat_P[i] = 0  # No power change
        if i == 0:
            soc[0] = soc_0  # Maintain initial SoC
        else:
            soc[i] = soc[i-1]  # Maintain previous SoC

        

# Print the final state of charge
print() # <--- Add a print statement to display the final state of charge. 