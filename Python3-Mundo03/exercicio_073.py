""" CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL,
NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
A) APENAS OS 5 PRIMEIROS COLOCADOS.
B) OS ÚLTIMOS 4 COLOCADOS DA TABELA.\
C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA.
D) EM QUE POSIÇÃO NA TABELA ESTÁ A CHAPECOENSE.
"""

brasileirao = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians",
               "Bragantino", "Fluminense", "América-MG", "Atletico-GO", "Santos",
               "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá",
               "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")

print(("\033[33m=+= \033[m")* 30)
print(f"Os 5 primeiros colocados são: \n{brasileirao[0:5]}")
print(("\033[31m=+= \033[m")* 30)
print(f"Os quatro rebaixados são: \n{brasileirao[-4:]}")
print(("\033[34m=+= \033[m")* 30)
print(f"Em ordem alfabética: \n{sorted(brasileirao)}")
print(("\033[36m=+= \033[m")* 30)
print(f"a Chapecoense está na posição: {brasileirao.index('Chapecoense')+ 1}ª")
print(("\033[32m=+= \033[m")* 30)

###################################################################################################

for time in brasileirao:
    print(time)