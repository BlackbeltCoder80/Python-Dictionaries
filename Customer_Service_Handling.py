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
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def service_tickets_menu():
    ticket_menu = []
    for ticket_id, details in service_tickets.items():
        ticket_menu.append([ticket_id, details["Customer"], details["Issue"], details["Status"]])
        print(tabulate(ticket_menu, headers=["Ticket ID", "Customer", "Issue", "Status"], tablefmt="grid",))

service_tickets_menu()



#NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

#The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.



