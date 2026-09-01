preguntas = ("¿Cuál es el planeta más grande del sistema solar?",
             "¿Cuál es la capital de Francia?",
             "¿Cuántos continentes hay?",
             "¿Quién pintó la Mona Lisa?",
             "¿Cuál es el océano más grande?")

opciones = (("A) Marte", "B) Júpiter", "C) Saturno", "D) Venus" ),
            ("A) Madrid", "B) Roma", "C) Paris", "D) Berlin" ),
            ("A) 5", "B) 6", "C) 7", "D) 8" ),
            ("A) Picasso", "B) Van Gogh", "C) Da Vinci", "D) Miguel Ángel" ),
            ("A) Atlántico", "B) Índico", "C) Ártico", "D) Pacifico" ))

respuestas = ("B","C","C","C","D")
intentos=[]
num_pregunta = 0
score = 0
for pregunta in preguntas:
    print(f"-------PREGUNTA #{num_pregunta+1}----------")
    print(pregunta)
    for opcion in opciones[num_pregunta]:
        print(opcion)
    intento = input("Ingrese su respuesta: ").upper()
    intentos.append(intento)
    if intento == respuestas[num_pregunta]:
        print(f"Respuesta Correcta #{num_pregunta + 1}")
    else:
        print(f"Respuesta Incorrecta #{num_pregunta + 1}")
    num_pregunta += 1

inte = 0
print("-------------------------------------")

for intento in intentos:
    if intento == respuestas[inte]:
        print(f"Respuesta Correcta #{inte +1} con una respuesta {intento}")
        score +=1
    else:
        print(f"Respuesta Incorrecta #{inte+1} con una respuesta {intento}")
    inte +=1

score = float(score / len(preguntas) * 100)
print(f"--Obtuviste un porcentaje de {score:.2f} % de respuestas correctas!!--")