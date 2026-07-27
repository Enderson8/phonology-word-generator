import random


# =========================
# FONOLOGIA
# =========================

consoantes = [
    "m", "n", "p", "t", "k",
    "s", "l", "r", "v", "z"
]

vogais = [
    "a", "e", "i", "o", "u"
]


# =========================
# CRIAÇÃO DE SÍLABAS
# =========================

def criar_silaba():

    inicio = ""

    if encontro_consonantal:

        if random.choice([True, False]):
            inicio = random.choice(consoantes) + random.choice(consoantes)

        else:
            inicio = random.choice(consoantes)

    else:

        inicio = random.choice(consoantes)


    nucleo = random.choice(vogais)


    if encontro_vocalico:

        if random.choice([True, False]):

            nucleo += random.choice(vogais)


    return inicio + nucleo



# =========================
# GERAR PALAVRA
# =========================

def gerar_palavra():

    palavra = ""

    for i in range(numero_silabas):

        palavra += criar_silaba()


    return palavra



# =========================
# CONFIGURAÇÃO
# =========================


numero_silabas = int(
    input("Quantas sílabas terá a palavra? ")
)


resposta = input(
    "Permite encontros consonantais? (s/n): "
)

encontro_consonantal = resposta.lower() == "s"



resposta = input(
    "Permite encontros vocálicos? (s/n): "
)

encontro_vocalico = resposta.lower() == "s"



# =========================
# RESULTADO
# =========================

print("\nPalavra criada:")

print(gerar_palavra())