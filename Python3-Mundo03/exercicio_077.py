""" CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS(NÃO USAR ACENTOS).
DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS."""

#VOGAIS = (A, E, I, O, U)

palavras = ("Leopardo", "Lagosta", "Canguru", "Gato",
            "Ganso", "Galo", "Mosquito", "Sapo",
            "Mula", "Corvo", "Avestruz")
for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos ", end="")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")
