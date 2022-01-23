""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção 'sem usar o sort()'.
No final, mostre a lista ordenada na tela."""


listaNum = []
num = 0
menor = 0
maior = 0
for cont in range(0, 5):
    num = int(input("Digite um número: "))
    if cont == 0 or num > listaNum[- 1]:
        listaNum.append(num)
        print("Adicionado ao final da lista.")
    else:
        posicao = 0
        while posicao < len(listaNum):
            if num <= listaNum[posicao]:
                listaNum.insert(posicao, num)
                print(f"Adicionado na posição {posicao}")
                break
            posicao += 1
print("\033[31m-=-\033[m" * 20)
print(f"Os valores digitados em ordem foram {listaNum}")
print("\033[31m-=-\033[m" * 20)
