from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Convert the string dates to datetime objects for comparison
    # Removing "th", "st", "nd", "rd" from the date strings to make them compatible with '%d %B' format
    todays_date = datetime.strptime(todays_date.replace("th", "").replace("st", "").replace("nd", "").replace("rd", ""), '%d %B')
    scheduled_date = datetime.strptime(scheduled_date.replace("th", "").replace("st", "").replace("nd", "").replace("rd", ""), '%d %B')

    # Compare the dates
    if todays_date > scheduled_date:
        return "Scheduled date has passed"
    elif todays_date < scheduled_date:
        return "Scheduled date is yet to pass"
    else:
        return "Scheduled date is today"

# Test cases
test1 = date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
test2 = date_passed("26th March", "26th March")  # Expected: Scheduled date is today
test3 = date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass

test1, test2, test3

print(date_passed("26th March", "25th March"))