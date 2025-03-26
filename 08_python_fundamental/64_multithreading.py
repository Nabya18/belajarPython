"""
# Multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I?O bound tasks like reading files or fetching data from APIs
# Bad for CPU bound tasks like rendering videos or playing games
# threading.Thread(target=my_function)
"""

import threading
import time


def walk_dog(first):
    time.sleep(8)
    print(f"You finished walking {first}")

def take_out_trash():
    time.sleep(2)
    print("You finished taking out the trash")

def get_mail():
    time.sleep(4)
    print("You finished getting the mail")

chore1 = threading.Thread(target=walk_dog, args=("Max",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# need chores finidhed before print "All chores are done"
chore1.join()
chore2.join()
chore3.join()

print("All chores are done") # this will be printed first because the chores are running concurrently