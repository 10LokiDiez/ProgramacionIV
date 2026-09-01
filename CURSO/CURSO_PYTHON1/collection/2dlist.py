fruits = ["apple", "pear", "orange","banana"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0])
print(groceries[0][1])

groceries2 = [["apple", "pear", "orange","banana"],
              ["celery", "carrots", "potatoes"], 
              ["chicken", "fish", "turkey"]]
print("_________________________________-")
for collection in groceries2:
    for object in collection:
        print(object, end=", ")
    print()