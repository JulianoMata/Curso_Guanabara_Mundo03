""" CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA.
NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.
"""
listagem = ( "macarrao", 8.00,
             "feijão", 9.80,
             "arroz", 18.95,
             "alho", 7.80,
             "cebola", 6.30)

print("-=-" * 14)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-=-" * 14)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f"{listagem[posicao]:.<30}", end="")
    else:
        print(f"R${listagem[posicao]:>7.2f}")
print("-=-" * 14)