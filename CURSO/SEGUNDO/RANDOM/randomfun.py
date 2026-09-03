import random

# print(help(random)) Para ver lo que hace

num = random.randint(1,100)
print(num)

options =("rock", "paper", "scissors")
op = random.choice(options)
print(op)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A",]
random.shuffle(cards)
print(cards)