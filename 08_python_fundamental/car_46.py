class car:
    def __init__(self, model, year, color, for_sale): # constructor method, self = reference to the current instance of the class
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving {self.color} {self.model}")

    def stop(self):
        print(f"You have stopped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.color} {self.model} ({self.year})")