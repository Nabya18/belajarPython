weight = float(input("Enter your weight: "))
unit = input("Kilograms(K) or pounds(L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}") # kalau di bawah walaupun tidak valid akan di cetak
else:
    print(f"{unit} was not valid")