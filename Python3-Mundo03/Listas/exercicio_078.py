"""Faça um programa que leia '5' valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o 'maior' e o 'menor' valor digitado e as suas
respectivas posições na lista"""


listaNum = []
maior = 0
menor = 0

for cont in range(0, 5):
    listaNum.append(int(input(f"Digite um valor para a Posição {cont}: ")))
    if cont == 0:
        maior = menor = listaNum[cont]
    else:
        if listaNum[cont] > maior:
            maior = listaNum[cont]
        if listaNum[cont] < menor:
            menor = listaNum[cont]
print("=-" * 30)
print(f"Você digitou os valores \033[35m{listaNum}\033[m")
print(f"O maior número é \033[34m{maior}\033[m nas posições ", end="")
for indice, valor in enumerate(listaNum):
    if valor == maior:
        print(f"\033[34m{indice}... \033[m ", end="")
print()
print(f"O menor número é \033[31m{menor}\033[m nas posições ", end="")
for indice, valor in enumerate(listaNum):
    if valor == menor:
        print(f"\033[31m{indice}... \033[m", end="")
print()




