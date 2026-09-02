username = input("Ingrese su usuario: ")
if len(username) > 12:
    print("El usuario es invalido, mas de 12 caracteres")
elif username.find(" ") != -1:
    print("El usuario es invalido, espacio detectado")
elif username.isalpha() == False:
    print("El usuario es invalido, contiene numeros")
else:
    print("Ingresando...")