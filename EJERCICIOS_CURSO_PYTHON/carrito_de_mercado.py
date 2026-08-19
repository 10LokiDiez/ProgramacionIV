item = input("Que objeto va a comprar? ")
price= float(input("Cual es el precio del objeto? "))
quantity = int(input("Cantos quieres? "))
total = price * quantity

print(f"Acabas de comprar {quantity} {item}/s a {price}$")
print(f"Para un total de {total}$")