""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas valores
'pares' e os valores 'ímpares' digitados, respectivamente.
Ao final, mostre o conteúdo das tres listas geradas.
EXTRA: coloquem em ordem crescente"""

# listaNum = []
# pares = []
# impares = []
# while True:
#     num = (int(input("Digite um número: ")))
#     listaNum.append(num)
#     opcao = str(input("Deseja continuar? [S/ N] ")).upper().strip()
#     if opcao != "S":
#         break
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)
#
# print("\033[31m+-+\033[m" * 20)
# print(f"A lista completa é \033[35m{listaNum}\033[m")
# print(f"A lista de pares é \033[36m{pares}\033[m")
# print(f"A lista de ímpares é \033[37m{impares}\033[m")

###################################### OUTRA MANEIRA ################################################

listaNum = list()
pares = list()
impares = list()
while True:
    listaNum.append(int(input("Digite um número: ")))
    listaNum.sort()
    opcao = str(input("Quer continuar? [S/N] ")).upper().strip()
    if opcao == "N":
        break
for indice, valor in enumerate(listaNum):
    if valor % 2 == 0:
        pares.append(valor)
        pares.sort()
    elif valor % 2 == 1:
        impares.append(valor)
        impares.sort()
print("\033[31m+-+\033[m" * 20)
print(f"A lista completa é \033[35m{listaNum}\033[m")
print(f"A lista de pares é \033[36m{pares}\033[m")
print(f"A lista de ímpares é \033[37m{impares}\033[m")


