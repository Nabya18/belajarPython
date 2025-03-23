"""
# exception = An event that interrupts the flow of a program
(ZeroDivisionError, ValueError, TypeError, exception ,etc.)
1. try, 2. except, 3. finally
"""

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You Cannot divide by zero")
except ValueError:
    print("Enter only a number")
except Exception:
    print("Something went wrong")
finally: # always executed
    print("Do something cleanup here")