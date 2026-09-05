#LISTAS
numbers1 = [1, 2, 3, 4, 5]

for number in numbers1:
    print(number, end = " ")

print()

for number in reversed(numbers1):
    print(number, end = " ")

print(end="\n\n")
#TUPLAS
numbers2 = (1, 2, 3, 4, 5)

for number in numbers2:
    print(number, end = " ")

print()

for number in reversed(numbers2):
    print(number, end = " ")

print(end="\n\n")


#SETS
numbers3 = {1, 2, 3, 4, 5}

for number in numbers3:
    print(number, end = " ")

print()

"""
for number in reversed(numbers3):
    print(number, end = " ")
NO SE PUEDEEEE YA QUE NO SE PUEDE CAMBIAR
        """

print(end="\n\n")

#STRING
name = "Simon Diez"

for caracter in name:
    print(caracter, end="  ")
print(end="\n\n")

#DICTIONARY
my_dictionary= {1:"A", 2:"B", 3:"C",}

for key in my_dictionary:
    print(key, end=" ")
""" o de esta forma
for key in my_dictionary.keys():
    print(key, end=" ")
"""
for value in my_dictionary.values():
    print(value, end=" ")
    
print()

for key, value in my_dictionary.items():
    print(f"{key} : {value}")