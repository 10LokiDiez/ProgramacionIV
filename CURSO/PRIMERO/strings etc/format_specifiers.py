price1 = 3.1416
price2 = 2342.243
price3 = -132.34

print(f"your price 1 is ${price1:2f}")
print(f"your price 2 is ${price2:2f}")
print(f"your price 3 is ${price3:2f}")
print("--------------------------------")
#10 CARACTERES
print(f"your price 1 is ${price1:10}")
print(f"your price 2 is ${price2:10}")
print(f"your price 3 is ${price3:10}")
print("--------------------------------")
#CON 0
print(f"your price 1 is ${price1:010}")
print(f"your price 2 is ${price2:010}")
print(f"your price 3 is ${price3:010}")
print("--------------------------------")
#JUSTIFICADOS
print(f"your price 1 is ${price1:<10}")
print(f"your price 2 is ${price2:>10}")
print(f"your price 3 is ${price3:^10}")
print("--------------------------------")
#POR MILES
print(f"your price 1 is ${price1:,}")
print(f"your price 2 is ${price2:,}")
print(f"your price 3 is ${price3:,}")
print("--------------------------------")
#SE PUEDEN JUNTAR ( CON SIGNO, CON SEPARADOR DE MILES Y CON2 DECIMALES)
print(f"your price 1 is ${price1:+,.2f}")
print(f"your price 2 is ${price2:+,.2f}")
print(f"your price 3 is ${price3:+,.2f}")
print("--------------------------------")