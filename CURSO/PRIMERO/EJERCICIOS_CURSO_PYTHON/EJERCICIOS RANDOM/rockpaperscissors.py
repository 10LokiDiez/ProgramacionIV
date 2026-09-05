import random

items = ["rock", "paper", "scissors"]
pointsbot = 0
points =0
print("ROCK PAPER SCISSORS GAME! EL QUE GANE 3 GANA!")
while True:
    option =  input(f"Cual opcion quiere escoger {items}: ").lower()
    optionbot = random.choice(items)

    if option not in items:
        print("Opcion Incorrecta")
        continue
    if option == optionbot:
        print(f"Es un empate los dos pusieron {option}")
    elif option == "rock" and optionbot == "paper":
        points += 1
        print(f"Ganaste! + 1 Tus puntos:{points} Bot: {pointsbot}")
    elif option == "paper" and optionbot == "rock":
        points += 1
        print(f"Ganaste! + 1 Tus puntos:{points} Bot: {pointsbot}")
    elif option == "scissors" and optionbot == "paper":
        points += 1
        print(f"Ganaste! + 1 Tus puntos:{points} Bot: {pointsbot}")
    elif option == "paper" and optionbot == "scissors":
        pointsbot += 1
        print(f"Perdiste Tus puntos:{points} Bot: {pointsbot}")
    elif option == "rock" and optionbot == "paper":
        pointsbot += 1
        print(f"Perdiste Tus puntos:{points} Bot: {pointsbot}")
    else:
        pointsbot += 1
        print(f"Perdiste Tus puntos:{points} Bot: {pointsbot}")

    if points == 3:
        print("GANASTE!!!")
        break

    if pointsbot ==3:
        print("PERDISTE!!!")
        break
    
