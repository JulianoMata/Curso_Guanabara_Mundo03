""" DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES DO TECLADO E GUARDE-OS NUMA TUPLA. NO FINAL, MOSTRE:
A) QUANTAS VEZES APARECEU O VALOR '9'.
B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR '3'.
C) QUAIS FORAM OS NÚMEROS PARES.
"""

numeros = (int(input("Digite um número: ")),
           int(input("Digite um número: ")),
           int(input("Digite um número: ")),
           int(input("Digite um número: ")))
print(f"Você digitou os valores {numeros}")
print(f"O valor '9' apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O valor '3' apareceu pela primeira vez na {numeros.index(3)+ 1}ª posição")
else:
    print("o valor '3' não foi digitado em nenhuma posição." )
print("Os valores pares digitados foram ", end="")
for num in numeros:
    if num % 2 == 0:
        print(num, end=" " )