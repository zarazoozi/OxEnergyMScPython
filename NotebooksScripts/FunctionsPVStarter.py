"""
Functions, Classes and Modules Tutorial
This file demonstrates Python functions.

Learning objectives:
- Defining and using functions

Complete the script by filling in the missing code sections marked with <---.

@author: PLACE YOUR NAME HERE
"""

# Import any necessary libraries
import math
import pandas as pd
import numpy as np
import os

# <--- Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size(): # <--- include parameters for building length, width, roof angle, panel width, panel height and panel power
    """
    This is a docstring. Use it to describe the function's purpose, parameters, and return values.
    """



    return # <--- return the total PV capacity in kW and number of panels

if __name__ == "__main__":
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
    
    pv_capacity_kw, num_panels = # <--- call the calculate_pv_size function with appropriate arguments

    print() # <--- Add a print statement to display the number of PV panels and the total PV capacity in kW
