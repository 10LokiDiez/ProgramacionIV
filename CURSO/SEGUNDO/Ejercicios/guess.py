import random
low = 1
high=100
print(f"--------ADIVINA EL NUMERO RANDOM DEL {low} HASTA EL {high}--------")
number = random.randint(low,high)
intentos = 0
while True:
    guess = input("Escriba el numero que crea que es: ")

    if not guess.isdigit():
        print("DATO ERRONEO")
        continue
    elif int(guess) == number:
        intentos += 1
        print(f"DATO CORRECTO ES {number} CON {intentos} INTENTOS")
        break
    elif int(guess) > number and int(guess) < high +1:
        intentos += 1
        print("El numero es menor")
    elif int(guess) < number and int(guess) > low:
        intentos += 1
        print("El numero es mayor")
    else:
        print(f"Tu numero esta fuera del rango escribe un dato entre {low} y {high}")
    