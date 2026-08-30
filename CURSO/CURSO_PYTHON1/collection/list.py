"""
List = [] ordenada y se pueden cambiar, si duplicados
"""
#LIST
fruits = ["apple","orange","pineapple","coconut"]
print(fruits)
print(fruits[3])
print(fruits[:2])
#[INICIO:FIN:PASO]

for fruit in fruits:
    print(fruit)

#dir(fruits) metodos funciones etc de listas
#o help(fruits)
print("---------------------------")
fruits[0] = "banana"
fruits.append("orange")
fruits.remove("pineapple")
fruits.insert(5, "kiwi")
for fruit in fruits:
    print(fruit)
print(len(fruits))
print("kiwi" in fruits)

#fruits.sort() organizar alfabeticamente
#fruits.reverse() organizar alreves
#fruits.clear limpiar toda la lista
print(fruits.index("orange")) #dice en que ubi esta la primera
print(fruits.count("orange")) #cuenta cuantas tiene