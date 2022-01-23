""" Crie um programa em que o usuário possa digitar vários valores numéricos e
 cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados em ordem crescente."""


listaNum = []
while True:
    num = int(input("Digite um número: "))
    if num not in listaNum:
        listaNum.append(num)
        print("Número adicionado com sucesso...")
    else:
        print("Número duplicado! Não vou adicionar...")
    opcao = str(input("Quer continuar? [S/N] ")).upper().strip()
    if opcao != "S":
        break

print("\033[32m-=-\033[m" * 20)
listaNum.sort()
print(f"Você digitou os valores {listaNum}")


