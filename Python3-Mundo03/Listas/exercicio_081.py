""" Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitador.
B) A lista de valores ordenada de forma decrescente e crescente.
C) Se o valor '5' foi digitado e está ou não na lista"""


listaNum = []

while True:
    listaNum.append(int(input("Digite um numero: ")))
    opcao = str(input("Deseja continuar? [S/N] \n")).upper().strip()
    if opcao != "S":
        break

print("\033[32m=-=\033[m" * 20)
print(f"Você digitou {len(listaNum)} números")
listaNum.sort(reverse=True)
print(f"Na ordem decrescente os números são {listaNum}")
listaNum.sort()
print(f"Na ordem crescente os números são {listaNum}")
if 5 in listaNum:
    print("O número '5' faz parte da lista!")
else:
    print("O número '5' não está na lista!")
print("\033[32m=-=\033[m" * 20)
