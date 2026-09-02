foods = []
prices = []
total = 0
while True:
    comida = input("Escriba la comida que quiera comprar (Continuar? N para salir): ")

    if comida.upper() == "N":
        break
    else:
        precio = float(input(f"Escriba el precio de una {comida}: "))
        prices.append(precio)
        foods.append(comida)

print("ESTA ES SU FACTURA")
for food in foods:
    print(food, end=" ")
    print(f"{prices[foods.index(food)]:,.2f}$")

for price in prices:
    total += price

print(f"SU TOTAL DE COMPRA ES {total:,.2f}$")