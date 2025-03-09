# logical operator = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

temp = -5
is_sunny = False
is_raining = False

# or
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# and
if temp >= 28 and is_sunny:
    print("It is HOT outside today")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside today")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny: # temp < 28 and temp > 0
    print("It is WARM outside today")
    print("It is SUNNY")
# not
elif temp >= 28 and not is_sunny:
    print("It is HOT outside today")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside today")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside today")
    print("It is CLOUDY")