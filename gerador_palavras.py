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
estruturas_silabicas = []

# =========================
# CRIAÇÃO DE SÍLABAS
# =========================

def criar_silaba():

    estrutura = random.choice(estruturas_silabicas)

    silaba = ""

    for elemento in estrutura:

        if elemento == "C":
            silaba += random.choice(consoantes)

        elif elemento == "V":
            silaba += random.choice(vogais)

    return silaba


# =========================
# GERAR PALAVRA
# =========================

def gerar_palavra():

    palavra = ""

    for i in range(numero_silabas):

        palavra += criar_silaba()


    return palavra
def gerar_vocabulario(quantidade):

    palavras = []

    for i in range(quantidade):
        palavras.append(gerar_palavra())

    return palavras

# =========================
# GERAR VOCABULÁRIO
# =========================

def gerar_vocabulario(quantidade):

    palavras = []

    while len(palavras) < quantidade:

        nova_palavra = gerar_palavra()

        if nova_palavra not in palavras:

            palavras.append(nova_palavra)

    return palavras

# =========================
# SALVAR VOCABULÁRIO
# =========================

def salvar_vocabulario(vocabulario):

    with open("vocabulario.txt", "w", encoding="utf-8") as arquivo:

        arquivo.write("VOCABULÁRIO GERADO\n")
        arquivo.write("==================\n\n")

        for i, palavra in enumerate(vocabulario, start=1):

            arquivo.write(f"{i}. {palavra}\n")

# =========================
# CONFIGURAÇÃO
# =========================


numero_silabas = int(
    input("Quantas sílabas terá a palavra? ")
)
quantidade_palavras = int(
    input("Quantas palavras deseja gerar? ")
)

resposta = input(
    "Permite encontros consonantais? (s/n): "
)

encontro_consonantal = resposta.lower() == "s"



resposta = input(
    "Permite encontros vocálicos? (s/n): "
)

encontro_vocalico = resposta.lower() == "s"

estruturas_silabicas.append("CV")


if encontro_consonantal:
    estruturas_silabicas.append("CCV")
    estruturas_silabicas.append("CVC")


if encontro_vocalico:
    estruturas_silabicas.append("CVV")

# =========================
# RESULTADO
# =========================

vocabulario = gerar_vocabulario(quantidade_palavras)

print("\nVocabulário gerado:\n")

for i, palavra in enumerate(vocabulario, start=1):

    print(f"{i}. {palavra}")

    salvar_vocabulario(vocabulario)

print("\nVocabulário salvo em 'vocabulario.txt'.")