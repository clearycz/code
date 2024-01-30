def speeding_ticket(speed, is_birthday):
    # Adjust speed limits if it's the driver's birthday
    speed_limit_adjustment = 5 if is_birthday else 0

    # Evaluate the ticket category based on speed
    if speed <= 60 + speed_limit_adjustment:
        return "No Ticket"
    elif 61 <= speed <= 80 + speed_limit_adjustment:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Test cases
test1 = speeding_ticket(60, False)  # Expected output: "No Ticket"
test2 = speeding_ticket(75, False)  # Expected output: "Small Ticket"
test3 = speeding_ticket(85, False)  # Expected output: "Big Ticket"
test4 = speeding_ticket(65, True)   # Expected output: "No Ticket"
test5 = speeding_ticket(85, True)   # Expected output: "Small Ticket"

test1, test2, test3, test4, test5

