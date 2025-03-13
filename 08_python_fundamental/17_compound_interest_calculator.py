# compund interest calculator = menghitung bunga majemuk

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than 0")
    else:
        break

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate of interest must be greater than 0")
    else:
        break # break = keluar dari loop

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than 0")
    else:
        break

total = principle * pow((1 + rate / 100), time) # pow = pangkat
print(f"The total amount after {time} years is: ${total:.2f}") # 2 angka dibelakang koma