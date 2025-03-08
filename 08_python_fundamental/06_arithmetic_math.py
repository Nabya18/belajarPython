# Arithmetic

friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
remainder = friends % 2

print(friends)
print(remainder)

# Math Functions
x = 3.14
y = -4
z = 5

# result = round(x) # dibulatkan
# result = abs(y) # nilai absolut
# result = pow(z, 2) # pangkat = 25
# result = max(x, y, z)
# result = min(x, y, z)
#
# print(result)


# Math
import math

print(math.pi)
print(math.e) # bilangan euler: konstanta matematika yang bernilai sekitar 2,71828 dan merupakan basis logaritma natural
# result = math.sqrt(9) # akar
# result = math.ceil(3.1) # pembulatan ke atas lawan dari round/floor
result = math.floor(3.9) # pembulatan ke bawah

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(result)
print(f"The circumference of the circle is {round(circumference, 2)}cm")
print(f"The area of the circle is {round(area, 2)}cm\u00b2") # \u00b2 = superscript 2
print(f"The hypotenuse of the triangle is {round(c, 2)}cm")