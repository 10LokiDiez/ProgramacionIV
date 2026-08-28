#[start : ende : step]
credit_number = "312432-32424-234234"

print(credit_number[2])
print(credit_number[0:5])
print(credit_number[:5])
print(credit_number[2:5])
print(credit_number[7:])
print(credit_number[-1])
print(credit_number[::2])

#CREATE A PROGRAM THAT GETS THE LAST 4 DIGITS OF A CREDIT CARD

number = "3242-5644-3456-8679"
last_number = number[-4:]
print(f"XXXX-XXXX-XXXX-{last_number}")

inverted_number = number[::-1]
print(inverted_number)