"""
# Match Case Statements (Switch): An alternative to if-elif-else statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable
"""


# case 'int'
def day_of_week(day):
    match day:
        case 1:
            return "It's Monday"
        case 2:
            return "It's Tuesday"
        case 3:
            return "It's Wednesday"
        case 4:
            return "It's Thursday"
        case 5:
            return "It's Friday"
        case 6:
            return "It's Saturday"
        case 7:
            return "It's Sunday"
        case _: # wild card
            return "Invalid day"

print(day_of_week(1))


# case 'string'
def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return "Yes, it's the weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "No, it's a weekday"
        case _: # wild card
            return False

print(is_weekend("Sunday"))