from random import randint

for x in range(1,6):
    gassnumber= int(input("Gass Number 1-5 :"))
    rengomNumber= randint(1,5)

    if gassnumber==rengomNumber:
        print("win")

    else:
        print("loss")