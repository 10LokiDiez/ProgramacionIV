

def dia_de_la_semana(day):
    match day:
        case 1:
            return "Es Lunes"
        case 2:
            return "Es Martes"
        case 3:
            return "Es Miercoles"
        case 4:
            return "Es Jueves"
        case 5:
            return "Es Viernes"
        case 6:
            return "Es Sabado"
        case 7:
            return "Es Domingo"
        case _:
            return "Invalido"
        
print(dia_de_la_semana(1))
print(dia_de_la_semana("asd"))

def finde(day):
    match day:
        case "Sabado" | "Domingo":
            return True
        case _:
            return False
        
print(finde("Lunes"))
print(finde("Sabado"))