#Tuple = () Ordenado, sin cambios, si duplicados
#PARECIDA A LA LISTA, PERO SIRVE MAS POR LO RAPIDO
fruits = ("apple","orange","pineapple","coconut", "coconut")

print(fruits)
#dir(fruits) metodos funciones etc de sets
#o help(fruits)
print(len(fruits))
print(fruits.index("orange")) #dice en que ubi esta la primera
print(fruits.count("coconut")) #cuenta cuantas tiene

for fruit in fruits:
    print(fruit)