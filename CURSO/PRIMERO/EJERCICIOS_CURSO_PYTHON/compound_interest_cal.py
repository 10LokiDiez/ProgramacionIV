#A = P(1+r/n)^t
"""
A = FINAL AMOUNT
P = INITIAL PRINCIPAL BALANCE
r = interest rate
t = number of time periods
"""

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Ingrese su monto inicial: "))
    if principal <= 0:
        print("Valor equivocado (Más de 0)")
    else:
        break


while True:
    rate = float(input("Ingrese su interes: "))
    if rate <= 0:
        print("Valor equivocado (Más de 0)")
    else:
        break

while True:
    time = int(input("Ingrese su tiempo en años: "))
    if time <= 0:
        print("Valor equivocado (Más de 0)")
    else:
        break

print("DATOS TOMADOS: ")
print(f"principal = {principal:,.2f}$")
print(f"rate = {rate:.2f} %")
print(f"time = {time} años")

a = principal * pow(( 1 + (rate /100 )), time)
print(f"El balance termino en {a:,.2f} $")