# for x in range (0,10)
#(donde empieza, donde termina, step)
for x in range(1,11):
    print(x)

print("------------------------------")

for x in reversed(range(1,11)):
    print (x)

print("------------------------------")
credit_card = "3478-3457-4590-3489"

for number in credit_card:
    print(number)

print("------------------------------")
for x in range(1,21):
    if x == 13:
        continue
    print(x)

#continue sirve para que simplemente salte la iteracion, en cambio el break sirve para parar todo el loop