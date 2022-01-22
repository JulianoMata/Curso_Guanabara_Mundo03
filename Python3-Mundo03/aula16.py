lanche = ("Hamburguer", "Batata", "Pizza", "Pudim", "Frutas")
print(lanche[-4])
print(len(lanche))
##############################################################
for c in lanche:
    print(f"Eu vou comer {c}")
    if c == "Suco":
        print(f"Comer não!! Beber!! {c}")
print("Comi e bebi demais!!")

########################### range/len ####################################
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

########################## enumerate #################################
for posicao, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {posicao}")

######################### sorted #####################################
print(sorted(lanche))
