#AND OR y NOT para los operadores logicos, y sirve para agregarle mas condiciones

age = int(input("Porfavor digite su edad: "))

if age >= 18:
    print("Eres mayor de edad")
elif age < 0:
    print("INVALIDO")
else :
    print("Eres menor de edad")

resp = input("Quieres comida (S/N): ")

if resp.upper() == "S":
    print("Quieres comida")
elif resp.upper() == "N":
    print("No quieres comida")
else:
    print("ERROR")

en_venta = True
if en_venta:
    print("Esta en venta")
else :
    print("No esta en venta")