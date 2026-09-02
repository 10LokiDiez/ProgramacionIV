print("BIENVENIDO A LA CALCULADORA PYTHON")
operador= input("Introduzca un operador + - * /: ")
num1 = float(input("Introduzca el primer numero: "))
num2 = float(input("Introduzca el segundo numero: "))

if operador == "+":
    res = num1 + num2
elif operador == "-":
    res = num1 - num2
elif operador == "*":
    res = num1 * num2
elif operador == "/":
    res = num1 / num2
else:
    print("ERROR")

print(f"Su resultado es: {round(res,2)}")