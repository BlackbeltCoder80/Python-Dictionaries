#2. Python Programming Challenges for Customer Service Data Handling
#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested 
# collections and loops by creating a system to track customer service tickets.

#Problem Statement: Develop a program that:

#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.
#Example ticket structure:
from tabulate import tabulate
import random
# Service ticket layout
service_tickets = [
{"Ticket ID": "Ticket001", "Customer": "Alice", "Issue": "Login problem", "Status": "open"},
{"Ticket ID": "Ticket002", "Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}]


# Service Ticket Selection Menu
service_ticket_selection = [["\nWelcome to Service Ticket Section"],
                    ["1. Open a serivice ticket"],
                    ["2. View service ticket"],
                    ["3. Mark a service ticket as complete"],
                    ["4. Reopen Service Ticket"],
                    ["5. Quit"]]

def service_menu():
    print(tabulate(service_ticket_selection, tablefmt="grid" ))
    
# Open New Service Tickets
def open_service_tickets():
    #"""Create a new service ticket with a unique number."""
    user_cutomer = input("You are about to start a new service ticket. Please Enter Your First Name:")
    user_issuse = input("Please enter the issuse or problem you are having.:")
    ticket_id = f"Ticket{random.randint(1, 999):03d}"
    
    if user_cutomer and user_issuse:
        service_tickets.append({"Ticket ID":ticket_id,"Customer": user_cutomer, "Issue": user_issuse,"Status": "Open"})
        print(f"Your task 'Service Ticket'has been added successfully!")
    else:
        print("All info must be entered!")


# View Current Service Tickets
def service_tickets_menu():
    """Display all service tickets in a tabular format."""
    ticket_menu = []  # List to hold ticket data for tabulation

    for details in service_tickets:
        ticket_menu.append([
            details["Ticket ID"], 
            details["Customer"], 
            details["Issue"], 
            details["Status"]
        ])  # Appending ticket dictionary values as a list
    # Print using tabulate
    print(tabulate(ticket_menu, headers=["Ticket ID", "Customer", "Issue", "Status"], tablefmt="grid"))

# Complete Service Tickets
def complete_service_ticket():
    service_tickets_menu()
    try:
        ticket_id = (input("\nPlease enter the Ticket ID, (e.g Ticket000) you wish to mark completed: "))
        found = False
        for ticket in service_tickets: # Check if the number is valid
         if ticket["Ticket ID"] == ticket_id:
            ticket["Status"] ="Closed"
        print(f"\nTask '{ticket_id}' marked as Closed \u2705.")
        found = True
    except KeyError:
        print("\nInvalid input! Please enter the correct Ticket ID (e.g Ticket000)")


# Reopen Service Tickets
def reopen_service_ticket():
    service_tickets_menu()
    try:
        ticket_id = (input("\nPlease enter the Ticket ID, (e.g Ticket000) you wish to mark completed: "))
        found = False
        for ticket in service_tickets: # Check if the number is valid
         if ticket["Ticket ID"] == ticket_id:
            ticket["Status"] ="Reopen"
        print(f"\nTask '{ticket_id}' marked as Reopend \u2705.")
        found = True
    except KeyError:
        print("\nInvalid input! Please enter the correct Ticket ID (e.g Ticket000)")


# Main Program Loop for Service Tickets
while True:
    service_menu()
    choose_service = input("\nSelect a number: ")

    if choose_service == "1": # Open New Service Tickets
        open_service_tickets() 
    elif choose_service == "2": # View Tickets (Open/Closed)
        service_tickets_menu()
    elif choose_service == "3": # Complete Service Tickets
        complete_service_ticket()
    elif choose_service == "4": # Reopen Ticket
        reopen_service_ticket()
    elif choose_service == "5": # Exit Service Ticket Menu
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid input! Please enter a number between 1 and 5.")




#NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

#The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.



