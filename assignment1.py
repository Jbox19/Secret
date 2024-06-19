from random import randint

humpyang = input("Choose fold or unfold: ")
print("player picks", humpyang)
choice = {'fold': 1, 'unfold': 2}

c1 = randint(1,2)
c2 = randint(1,2)


print("c1 picks", c1)
print("c2 picks", c2)

if humpyang == 1 and c1 == 2 and c2 == 2:
    print("Player win")
elif humpyang == 2 and c1 == 1 and c2 == 2:
    print("c1 win")
elif humpyang == 2 and c1 == 2 and c2 == 1:
    print("c2 win")
else:
    print("draw")