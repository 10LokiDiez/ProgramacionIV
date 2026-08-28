name = input("Cual es tu nombre?: ")
#LONGITUD DE LA CADENA
caract = len(name)

print(caract)
#BUSCA DONDE ESTA LA o
ooo = name.find("o")
print(ooo)

#BUSCA DONDE ESTA LA ULTIMA o
ooof = name.rfind("o")
print(ooof)

print(name.capitalize())

uppername = name.upper()
print(uppername)

lowername = name.lower()
print(lowername)

result = name.isdigit()
print(result)

result2 = name.isalpha()
print(result2)

#.count() sirve para contar cuantos de esos hay, por ejemplo count("-")
#.replace() sirve para remplazar algo de algun string por ejemplo
# .replace("-", " ") quita los slash

tel = "4534-5435-4353433"

tel = tel.replace("-", "")

print(tel)

#print(help(str))  para ver las funciones