#diccionario {key: value}
# { llave: valor }
# la llave arroja un valor

capitals = {"USA" : "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Colombia": "Bogota"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("Colombia"))
print(capitals.get("Japan"))

if capitals.get("Japon"): 
    print("Esta capital existe")
else:
    print("Esta capital no existe")

#Sirve para actualizar o agregar nuevas llaves con valores
capitals.update({"Germany":"Berlin"})

#Metodo que elimina la llave entera
capitals.pop("China")

#capitals.clear limpia todo el diccionario

###########
print("---------------------------")
print(capitals.keys())

for key in capitals.keys():
    print(key)

print("---------------------------")
print(capitals.values())

for value in capitals.values():
    print (value)

print("---------------------------")

print(capitals.items())

for item in capitals.items():
    print(f"Pais: {item[0]}, Capital: {item[1]}")

print("------------OTRO MODO:---------------")
for key, item in capitals.items():
    print(f"Pais: {key}, Capital: {item}")