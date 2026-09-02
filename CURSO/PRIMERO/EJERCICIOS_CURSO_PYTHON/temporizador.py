import time
print("--------------TEMPORIZADOR----------------")
while True:
    print("1. Ingresar temporizador en segundos ")
    print("2. Ingresar temporizador individualmente (horas, minutos y segundos) ")
    print("------------------------------------------")
    op = int(input("Ingrese la opcion que desea: "))
    if op == 1 or op == 2:
        break
    else:
        print("DATO ERRONEO")
        
if op == 1:
    sec = int(input("Ingrese los segundos del temporizador: "))
    for x in range(sec,0,-1):
        seg = x % 60
        minu = int(x / 60) % 60
        hou = int(x / 3600)
        print(f"{hou:02}:{minu:02}:{seg:02}")
        time.sleep(1)
    print("WAKE UP")
else:
    hour = int(input("Ingrese las horas: "))
    minuts = int(input("Ingrese los minutos: "))
    sec = int(input("Ingrese los segundos: "))

    sec = hour*3600 + minuts *60 + sec
    for x in range(sec,0,-1):
            seg = x % 60
            minu = int(x / 60) % 60
            hou = int(x / 3600)
            print(f"{hou:02}:{minu:02}:{seg:02}")
            time.sleep(1)
    print("WAKE UP")

