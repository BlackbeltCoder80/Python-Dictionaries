# 1. Real-World Python Dictionary Applications
# Objective: The aim of this assignment is to reinforce your understanding and application of 
# Python dictionaries, nested collections, and dictionary methods.

#Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. 
# Your task is to update this menu based on given instructions

#Problem Statement: Given the initial menu:
from tabulate import tabulate
restaurant_menu ={
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu["Breverages"] = {"Corona": 8.00, "Modelo": 4.00}
restaurant_menu["Main Course"]["Steak"] = 17.99
remove_restaurant_item = restaurant_menu["Starters"].pop("Bruschetta")

table_data = [] # Here Im creating a empty list for tabulate to create my rows.
for category, items in restaurant_menu.items(): # here im getting catagory "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    #"Main Course": {"Steak": 15.99, "Salmon": 13.99},
# Desserts": {"Cake": 4.99, "Ice Cream": 3.99} and its nested dicitonaries along with all the others
    #in restaurant_menu. 
    for item, price in items.items(): # get items and there prices. 
        table_data.append([category, item, f"${price:.2f}"]) # this adds the ditionary as a list 
        # IF you want a everything in the list with Bracers chagne item it items.
        #I didnt like the way it looked. So, i just palyed around with it. 

print(tabulate(table_data, headers=["CATEGORY", "ITEM", "PRICE"],tablefmt="grid")) # Creates Header table_data defined above: 
#The headers are listed as shown and must be written as you would like the them. 
# tablefmt="grid" is one along with several other outputs for tabulate. 
# Resource used : https://app.datacamp.com/learn/tutorials/python-tabulate

#print(tabulate(restaurant_menu))
#- Add a new category called "Beverages" with at least two items.

#- Update the price of "Steak" to 17.99.

#- Remove "Bruschetta" from "Starters". 