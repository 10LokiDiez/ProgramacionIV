lista = [x for x in range(1, 11)]
print(lista)

doubles = [x * 2 for x in range(1, 11)]
print(doubles)

squares = [x**2 for x in range (1,11)]
print(squares)

fruits = ["apple", "banana", "coconut", "orange"]

fruits = [fruit.upper() for fruit in fruits]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits)

print (fruits_chars)

numbers = [1,-2,3,-4,5,-6]
positive = [abs(number) for number in numbers]
print(positive)

just_positive = [number for number in numbers if number >=0]

print(just_positive)


calificaciones = [80, 95, 12, 54, 67, 93, 85, 79, 88]
                 #Por cada nota en calificaciones si la nota es mas o igual de 80, me devuelve las notas que si pasan
pasados = [ nota for nota in calificaciones if nota>=80]

print(pasados)