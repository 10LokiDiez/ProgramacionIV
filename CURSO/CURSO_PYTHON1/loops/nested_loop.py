#cuadrado
grande = int(input("Ingrese el tamaño del cuadrado: "))
for x in range(0,grande):
    for y in range(0,grande):
        print(f"* ", end="")
    print("", end="\n")
