#STRINGS
email = "sidimome@gmail.com"
if "@" in email and "." in email:
    print("CORREO VALIDO")
else:
    print("CORREO INVALIDO")

word = "APPLE"
letter = input("Adivina la letra en la palabra secreta: ").upper()
if letter in word: # se puede poner un not in, seria al reves
    print(f"si esta la palabra {letter}")
else:
    print(f'{letter} no esta en la palabra')
    
#TUPLAS LISTAS O SETS
students = {"Spongebob", "Patrick", "Sandy"}
student = input("Adivina el estudiante: ").capitalize()

if student in students:
    print(f"{student} si es un estudiante")
else:
    print(f"{student} no es un estudiante")
    

#DICTIONARIES

grados = {"Spongebob" : "A",
          "Patrick": "B" ,
          "Sandy": "C"}

estudiante = input("Escribe el estudiante: ").capitalize()

if estudiante in grados:
    print(f"El grado de {estudiante} es : {grados[estudiante]}")