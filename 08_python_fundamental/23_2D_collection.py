# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", 'potatoes'],
#              ["chicken", "fish", "turkey"]] # 2D list
#
# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#
#     print() # print a new line

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")) # 2D tuple

for row in num_pad:
    for num in row:
        print(num, end=" ")

    print() # print a new line