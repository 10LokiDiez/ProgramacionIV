age = int(input("DIGITA TU EDAD: "))

while age < 0:
    print("No es valido")
    age = int(input("Digita otra vez tu edad: "))
print(f"Tu edad es: {age}")