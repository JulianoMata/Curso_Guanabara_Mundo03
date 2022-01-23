num = [2, 5, 9, 1]
num[2] = 3
print(num)

num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(2, 2)
print(num)
print(f"Essa lista tem {len(num)} elementos.")

num.pop()
print(num)

num.pop(2)
print(num)

num.remove(2)
print(num)

if 4 in num:
    num.remove(4)
else:
    print("Não achei número 4")

####################################################################################################
# valores = list() ***PODE COMEÇAR UMA LISTA VAZIA DE DOIS MODOS***
valores = [15, 29, 34]

for valor in valores:
    print(f"\033[34m{valor}...\033[m\n", end="")

for cont in range(0, 3):
    valores.append(int(input("Digite um valor: ")))

for chave, valor in enumerate(valores):
    print(f"Na posição {chave} encontrei o valor {valor}!")
print("cheguei ao final da lista.")

#########################################################################################
a = [2, 3, 4, 7]
b = a  # faz uma ligação entre as listas
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

a = [2, 3, 4, 7]
b = a[:]  # cria uma cópia
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
