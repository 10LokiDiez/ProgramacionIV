#Set = {} desordenada y inmutable, agregar/eliminar OK
#No tiene duplicados

fruits = {"apple","orange","pineapple","coconut"}
#dir(fruits) metodos funciones etc de sets
#o help(fruits)
print(fruits)

for fruit in fruits:
    print(fruit)


#NO FUNCIONA EL INDEXING fruits[1]
print("---------------------------")
fruits.add("banana")
fruits.add("banana")
fruits.add("banana")

fruits.remove("pineapple")
print(len(fruits))
#fruits.clear limpia toda el set
#fruits.pop limpia el primero, pero siempre es random
for fruit in fruits:
    print(fruit)
