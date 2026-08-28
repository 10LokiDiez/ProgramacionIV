lon = int(input("Ingrese la longitud deseada: "))
symbol = input("Ingrese el simbolo que quiere utilizar: ")

print("1. rectangulo")
print("2. triangulo 1")
print("3. triangulo 2")
print("4. triangulo completo")
print("5. triangulo completo inverso")
print("6. rombo")
op = int(input("Que figura quieres hacer: "))

match op:
    case 1:
        for x in range(0, lon):
            for y in range( 0, lon):
                print(f"{symbol} ", end="")
            print("")
    case 2:
        for x in range(0, lon):
            for y in range(0, x + 1):
                print(f"{symbol} ", end="")
            print("")
    case 3:
        for x in range(0, lon):
            for y in range(0, lon- x):
                print("  ", end="")
                
            for y in range(y, lon):
                print(f"{symbol} ", end="")
            print("")
    case 4:
        temp = lon
        for x in range(0, lon):
            for y in range(0, lon- x):
                print("  ", end="")
        
            for y in range(y, temp):
                print(f"{symbol} ", end="")

            temp += 1 
            print("")
    case 5:
        temp = lon
        for x in range(1, lon):
            for y in range(1, x + 1):
                print(f"  ", end="")
            for z in range(0, temp  - x):
                print(f"{symbol} ", end="")
            for z in range(0, temp  - x - 1):
                print(f"{symbol} ", end="")
            print("") 
    case 6:
        temp = lon
        for x in range(0, lon):
            for y in range(0, lon- x):
                print("  ", end="")
        
            for y in range(y, temp):
                print(f"{symbol} ", end="")
        
            temp += 1 
            print("")

        temp = lon
        for x in range(1, lon):
            for y in range(0, x + 1):
                print(f"  ", end="")
            for z in range(0, temp - x):
                print(f"{symbol} ", end="")
            for z in range(0, temp  - x - 1):
                print(f"{symbol} ", end="")
            print("") 
