
#Esta mejorable se podria hacer mejor con los metodos de diccionario
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries" : 2.50,
        "chips" : 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25} 

cart= []
total = 0

print("----------------- BIENVENIDO -----------------")
for k, v in menu.items():
    print(f"{k.capitalize():10}  {v:.2f}$")

print("----------------------------------------------")

while True:
    product = input("Ingrese el producto que quiera (q para la factura): ").lower()
    vali= True
    quan= 1
    if product == "q":
        break
    else:
        for k, v in menu.items():
            if k == product:
                cart.append(product)
                quan= int(input("Que cantidad desea: "))
                print(f"{k.capitalize()} añadido al carrito con un valor de {v*quan:.2f}$")  
                total += v*quan
                vali = False
            else:
                continue
        if vali:
            print("Producto invalido")



print("----------------------------------------------")
print(f"        SU TOTAL DE COMPRA ES {total:,.2f}$")
print("----------------------------------------------")