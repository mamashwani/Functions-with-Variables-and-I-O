# -*- coding: utf-8 -*-
"""
Muhammad Mashwani
PeopleSoft ID: 1378052
COSC 1306 
Assignment #2
Homework #1 - First Look 
"""
SEALANT_COVERAGE = 6 #sealant covers 6m^2 per liter
LITERS_PER_BOTTLE = 2 #UltraBlocker comes in 2 liter bottles

def get_value(parameter):
    return int(input("Please enter a " + parameter))

def round_up(number):
    return int(number + 0.99) #To Do Fix this to actually work 

length = get_value("length(m): ")  
width = get_value("width(m): ")
cost = get_value("cost($): ")

area = length * width
l_of_sealant = round_up(area / SEALANT_COVERAGE) 
bottles_of_sealant = round_up(l_of_sealant / LITERS_PER_BOTTLE)
total_cost = bottles_of_sealant * cost

print()
print("="*40)
print("The area is: "+ str(area) + ".")
print("Volume of sealant needed is: " + str(l_of_sealant) + "L.")
print("Bottles of selant needed is: " + str(bottles_of_sealant) + ".")
print("Total cost is: " + "$" + str(total_cost))
print("="*40)

"""
Please enter a length(m): 137 (First three digits of my PeopleSoft ID )

Please enter a width(m): 8052 (Last 4 digits of my PeopleSoft ID)

Please enter a cost($): 26 (1+3+7+8+0+5+2 = 26)

========================================
The area is: 1103124.
Volume of sealant needed is: 183854L.
Bottles of selant needed is: 91927.
Total cost is: $2390102
========================================
"""