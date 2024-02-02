# EBEMS: E-Business Event Management System

# Import necessary libraries
# No external libraries required for this basic version

# Event Database: Stores event information
events_db = {}

# Feedback Database: Stores feedback for each event
feedback_db = {}

# Customer Loyalty Points Database: Tracks loyalty points for customers
customer_loyalty_points = {}

# Function to create or modify events
def manage_event(event_id, name=None, speaker=None, date=None, capacity=None, modify=False):
    """
    Creates or modifies an event based on the provided details.
    """
    if modify and event_id in events_db:
        # Modify existing event
        if name: events_db[event_id]['name'] = name
        if speaker: events_db[event_id]['speaker'] = speaker
        if date: events_db[event_id]['date'] = date
        if capacity: events_db[event_id]['capacity'] = capacity
        print("Event modified successfully.")
    elif not modify:
        # Create new event
        events_db[event_id] = {'name': name, 'speaker': speaker, 'date': date, 'capacity': capacity, 'attendees': []}
        print("Event created successfully.")
    else:
        print("Event ID not found for modification.")

# Function to register for an event
def register_for_event(event_id, customer_name):
    """
    Registers a customer for an event, if capacity allows.
    """
    if event_id in events_db and len(events_db[event_id]['attendees']) < events_db[event_id]['capacity']:
        events_db[event_id]['attendees'].append(customer_name)
        # Update loyalty points, assuming 10 points per registration
        customer_loyalty_points[customer_name] = customer_loyalty_points.get(customer_name, 0) + 10
        print(f"Registration successful for {customer_name}.")
    else:
        print("Registration failed. Event may be full or does not exist.")

# Function to search and manage events (cancel or unregister)
def search_and_manage_events(search_query):
    """
    Searches events by name or speaker, then offers options to cancel the event or unregister a customer.
    """
    found_events = {eid: details for eid, details in events_db.items() if search_query.lower() in details['name'].lower() or search_query.lower() in details['speaker'].lower()}
    if not found_events:
        print("No matching events found.")
        return
    
    # Display found events
    for eid, details in found_events.items():
        print(f"ID: {eid}, Name: {details['name']}, Speaker: {details['speaker']}, Date: {details['date']}, Capacity: {details['capacity']}, Attendees: {len(details['attendees'])}")
    
    # Choose an event to cancel or unregister from
    event_choice = input("Enter event ID to manage (cancel or unregister): ")
    if event_choice not in found_events:
        print("Invalid event ID.")
        return
    
    # Choose action
    action = input("Choose action - cancel event (c) or unregister a customer (u): ").lower()
    if action == 'c':
        # Cancel the event
        del events_db[event_choice]
        print(f"Event {event_choice} has been canceled.")
    elif action == 'u':
        # Unregister a customer from the event
        customer_name = input("Enter customer ID to unregister: ")
        if customer_name in events_db[event_choice]['attendees']:
            events_db[event_choice]['attendees'].remove(customer_name)
            print(f"Customer {customer_name} has been unregistered from event {event_choice}.")
        else:
            print("Customer ID not found in event attendees. Please try again.")

# Function to collect feedback
def collect_feedback(event_id, customer_name, feedback):
    """
    Collects feedback for an event from a customer.
    """
    if event_id in events_db:
        if event_id not in feedback_db:
            feedback_db[event_id] = []
        feedback_db[event_id].append({'customer_id': customer_name, 'feedback': feedback})
        print("Feedback collected successfully.")
    else:
        print("Invalid event ID. Please try agian")

# Function to generate reports
def generate_report(event_id):
    """
    Generates a report for an event, including attendance and feedback.
    """
    if event_id in events_db:
        event = events_db[event_id]
        print(f"Event Report for {event['name']}:")
        print(f"Date: {event['date']}, Speaker: {event['speaker']}, Capacity: {event['capacity']}, Attendees: {len(event['attendees'])}")
        if event_id in feedback_db:
            print("Feedback:")
            for feedback in feedback_db[event_id]:
                print(f"Customer {feedback['customer_id']}: {feedback['feedback']}")
    else:
        print("Event ID does not exist. Please try again")

# Function to display total loyalty points for a customer
def display_loyalty_points(customer_id):
    points = customer_loyalty_points.get(customer_id, 0)
    print(f"Customer {customer_id} has {points} loyalty points.")


# User Interface Function
def user_interface():
    """
    Provides a text-based user interface for managing the EBEMS.
    """
    while True:
        print("\nWelcome to the E-Business Event Management System (EBEMS)")
        print("1. Create or Modify Event")
        print("2. Register for Event")
        print("3. Search and Manage Events")
        print("4. Collect Feedback")
        print("5. Generate Report")
        print("6. Display Loyalty Points")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Event creation/modification
            event_id = input("Create event ID: ")
            name = input("Create event name: ")
            speaker = input("Enter speaker name: ")
            date = input("Enter event date(D/M/Y): ")
            capacity = int(input("Create event capacity: "))
            modify = input("Modify existing event? (yes/no): ").lower() == 'yes'
            manage_event(event_id, name, speaker, date, capacity, modify)
        elif choice == '2':
            # Registration
            event_id = input("Enter existing event ID: ")
            customer_name = input("Create your customer name: ")
            register_for_event(event_id, customer_name)
        elif choice == '3':
            # Search and manage events
            search_query = input("Search term (Enter existing event name or speaker name to show the details): ")
            search_and_manage_events(search_query)
        elif choice == '4':
            # Feedback collection
            event_id = input("Enter existing event ID for feedback: ")
            customer_name = input("Enter your customer name: ")
            feedback = input("Write your feedback: ")
            collect_feedback(event_id, customer_name, feedback)
        elif choice == '5':
            # Report generation
            event_id = input("Enter existing event ID to create report: ")
            generate_report(event_id)
        elif choice == '6':
            customer_name = input("Enter your customer name: ")
            display_loyalty_points(customer_name)
        elif choice == '0':
            # Exit
            print("Exiting EBEMS. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main entry point
if __name__ == "__main__":
    user_interface()
