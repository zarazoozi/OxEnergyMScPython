"""
Functions, Classes and Modules Tutorial
This file demonstrates Python functions, classes, and modules.

Learning objectives:
- Defining and using functions
- Creating and utilizing classes
- Importing and using modules

Complete the script by filling in the missing code sections marked with <---.

@author: PLACE YOUR NAME HERE
"""

# Import any necessary libraries
import math
import pandas as pd
import numpy as np
import os

# <--- Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size():



print() # <--- Add a print statement to display the number of PV panels and the total PV capacity in kW

class Storage_Asset(): # <--- convert your code from a1 into a storage asset class
    def __init__(self):

    def update_storage(self, t, demand_P, dt=1)
        
        return bat_p_t



class Demand_Asset():
    def __init__(self, name, T=8760, demand_profile=None):
        self.name = name
        self.T = T
        if isinstance(demand_profile, type(None)):
            self.demand_profile = [0] * 24  # Default to zero demand for 24 hours
        elif isinstance(demand_profile, list) and all(isinstance(i, (int, float)) for i in demand_profile):
            self.demand_profile = demand_profile
        elif isinstance(demand_profile, str) and os.path.isfile(demand_profile):
            self.demand_profile = pd.read_csv(demand_profile).squeeze().tolist()
        else:
            raise ValueError("Invalid demand profile")

class PV_Asset():
    def __init__(self, name, pv_capacity, T=8760, capacity_factor=None):
        self.name = name
        self.pv_capacity = pv_capacity
        self.T = T

        if isinstance(capacity_factor, type(None)):
            self.capacity_factor = [0.11] * self.T  # Default to 11% capacity factor
        elif isinstance(capacity_factor, list) and all(isinstance(i, (int, float)) for i in capacity_factor):
            self.capacity_factor = capacity_factor
        elif isinstance(capacity_factor, str) and os.path.isfile(capacity_factor):
            self.capacity_factor = pd.read_csv(capacity_factor).squeeze().tolist()
        else:
            raise ValueError("Invalid PV profile")

    def calculate_pv_output(self):
        pv_output = [self.pv_capacity * cf for cf in self.capacity_factor]
        return pv_output