import random

low = 1
high = 100
options= ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#number = random.randint(low, high) # return a random integer between 1 and 10
number = random.random() # return a random float between 0 and 1
option = random.choice(options) # return a random element from the list
random.shuffle(cards) # shuffle the list in place

print(number)
print(option)
print(cards)