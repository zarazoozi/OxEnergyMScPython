"""
Functions, Classes and Modules Tutorial
This file demonstrates Python functions.

Learning objectives:
- Defining and using functions

Complete the script by filling in the missing code sections marked with <---.

@author: Zara P :)
"""

# Import any necessary libraries
import math
#import pandas as pd
#import numpy as np
import os

#building_length_m = 30  # <--- Define building length in meters
#building_width_m = 10   # <--- Define building width in meters
#roof_angle_deg = 22     # <--- Define roof angle in degrees
#panel_width = 1032.0      # <--- Define panel width in mm
#panel_length = 1872.0     # <--- Define panel height in mm
#panel_thickness= 40.0
#panel_power_kw = 0.4   # <--- Define panel power in kW

# <--- Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size(building_length_m, building_width_m, roof_angle_deg, panel_width, panel_length, panel_thickness, panel_power_kw ): # <--- include parameters for building length, width, roof angle, panel width, panel height and panel power
    area_roof_m2 = (building_length_m * building_width_m )/math.cos(math.radians(roof_angle_deg))  
    panel_number = area_roof_m2 / ((panel_width/1000) * (panel_length/1000))  # <--- Calculate number of panels that fit on the roof
    voltage_from_PV= panel_power_kw * panel_number # <--- Calculate roof area considering roof angle
    return (panel_number, voltage_from_PV) # <--- return the total PV capacity in kW and number of panels

result = calculate_pv_size (30, 10, 22, 1032.0 ,1872.0 ,40.0 ,0.4) 
print(result) # <--- call the function with appropriate arguments

# if __name__ == "__main__":
    # =============================================================================
    # This section is a common way to incorporate code that you want to run if the 
    # script is executed directly, but will be ignored if the script is 
    # imported as a module into another. 
    # 
    # It separates the executable part of the script from the part that defines
    # reusable components e.g. functions.
    # 
    # This is useful way of testing the code or providing examples of how to 
    # use the code.
    # =============================================================================
    
   # pv_capacity_kw, num_panels = # <--- call the calculate_pv_size function with appropriate arguments

    ##print() # <--- Add a print statement to display the number of PV panels and the total PV capacity in kW
