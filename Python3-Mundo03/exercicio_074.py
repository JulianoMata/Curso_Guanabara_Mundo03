""" CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALETÓRIOS E COLOCAR EM UMA TUPLA.
DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR VALOR E O MAIOR VALOR
 QUE ESTÁ NA TUPLA."""

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"\033[33mOs valores sorteados foram: \033[m", end="")
for num in numeros:
    print(f"{num} ", end="")
print(f"\nO maior valor sorteado foi \033[31m{max(numeros)}\033[m")
print(f"O menor valor sorteado foi  \033[36m{min(numeros)}\033[m")
