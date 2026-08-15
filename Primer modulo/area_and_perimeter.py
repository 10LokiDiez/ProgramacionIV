import math 
side = float(input("Escriba cual es el lado de su rectangulo: "))
radius = float(input("Escriba cual es el radio de su circulo: "))

area_rec = side * side
per_rec = 4* side

area_cir = math.pi * radius **2
per_cir = 2.0 * math.pi * radius

print(f"The area of your rectagle is: {area_rec} and the perimeter is: {per_rec}" )
print(f"The area of your circle is: {area_cir} and the perimeter is: {per_cir}" )
