import random


# =========================
# FONOLOGIA
# =========================

consoantes = [
    "m",
    "n",
    "p",
    "t",
    "k",
    "s",
    "l",
    "r",
    "v",
    "z"
]

vogais = [
    "a",
    "e",
    "i",
    "o",
    "u"
]


def criar_silaba():
    return random.choice(consoantes) + random.choice(vogais)



def criar_palavra():

    quantidade = random.randint(2, 4)

    palavra = ""

    for i in range(quantidade):
        palavra += criar_silaba()

    return palavra



# =========================
# SEMÂNTICA
# =========================

conceitos = {

    "algo_vivo": {
    "classe": "substantivo",
    "pode_ser_agente": True,
    "pode_ser_objeto": False,
    "interage_com": [
        "agua",
        "comida",
        "abrigo"
    ]
},

    "agua": {
        "classe": "substantivo",
        "pode_ser_agente": False,
        "pode_ser_objeto": True
    },

    "fogo": {
        "classe": "substantivo",
        "pode_ser_agente": False,
        "pode_ser_objeto": True
    },

    "comida": {
        "classe": "substantivo",
        "pode_ser_agente": False,
        "pode_ser_objeto": True
    },

    "abrigo": {
        "classe": "substantivo",
        "pode_ser_agente": False,
        "pode_ser_objeto": True
    },

    "perigo": {
        "classe": "substantivo",
        "pode_ser_agente": False,
        "pode_ser_objeto": True
    },

    "movimento": {
        "classe": "verbo"
    }
}


# Criando o vocabulário

dicionario = {}


for conceito, dados in conceitos.items():

    palavra = criar_palavra()

    dicionario[palavra] = {
        "significado": conceito,
        "classe": dados["classe"],
        "pode_ser_agente": dados.get("pode_ser_agente", False),
        "pode_ser_objeto": dados.get("pode_ser_objeto", False)
    }

# Criando o vocabulário




dicionario = {}


for conceito, dados in conceitos.items():

    palavra = criar_palavra()

    dicionario[palavra] = {
        "significado": conceito,
        "classe": dados["classe"],
        "pode_ser_agente": dados.get("pode_ser_agente", False),
        "pode_ser_objeto": dados.get("pode_ser_objeto", False)
    }

# =========================
# RESULTADO
# =========================

print("Primeiro vocabulário da língua:\n")


for palavra, dados in dicionario.items():

    print(
        palavra,
        "=",
        dados["significado"],
        "(",
        dados["classe"],
        ")"
    )

# =========================
# GRAMÁTICA
# =========================

ordens_possiveis = [
    "SVO",
    "SOV",
    "VSO"
]


gramatica = random.choice(ordens_possiveis)


print("\nEstrutura gramatical da língua:")
print(gramatica)

# =========================
# EVENTOS E PAPÉIS SEMÂNTICOS
# =========================

def pegar_agente():

    possibilidades = []

    for palavra, dados in dicionario.items():

        if dados.get("pode_ser_agente"):

            possibilidades.append(
                dados["significado"]
            )

    return random.choice(possibilidades)



def pegar_objeto():

    possibilidades = []

    for palavra, dados in dicionario.items():

        if dados.get("pode_ser_objeto"):

            possibilidades.append(
                dados["significado"]
            )

    return random.choice(possibilidades)

print("\nDEBUG DO DICIONARIO")

for palavra, dados in dicionario.items():
    print(palavra, dados)

    def pegar_objeto_para_agente(agente):

    possibilidades = []

    for conceito, dados in conceitos.items():

        if conceito in conceitos[agente].get("interage_com", []):

            possibilidades.append(conceito)


    return random.choice(possibilidades)

def criar_evento():

    agente = pegar_agente()

    evento = {
        "agente": agente,
        "acao": "movimento",
        "objeto": pegar_objeto_para_agente(agente)
    }

    return evento

def traduzir_frase(frase):

    resultado = []

    for conceito in frase:

        for palavra, significado in dicionario.items():

           if significado["significado"] == conceito:
                resultado.append(palavra)

    return resultado


print("\nPrimeiro pensamento da língua:")

evento = criar_evento()

def organizar_frase(evento):

    if gramatica == "SVO":

        return [
            evento["agente"],
            evento["acao"],
            evento["objeto"]
        ]


    elif gramatica == "SOV":

        return [
            evento["agente"],
            evento["objeto"],
            evento["acao"]
        ]


    else:  # VSO

        return [
            evento["acao"],
            evento["agente"],
            evento["objeto"]
        ]

print(evento)


frase = organizar_frase(evento)


print("\nFrase na língua:")

print(traduzir_frase(frase))

def organizar_frase(evento):

    if gramatica == "SVO":

        return [
            evento["agente"],
            evento["acao"],
            evento["objeto"]
        ]


    elif gramatica == "SOV":

        return [
            evento["agente"],
            evento["objeto"],
            evento["acao"]
        ]


    else: # VSO

        return [
            evento["acao"],
            evento["agente"],
            evento["objeto"]
        ]
    print("\nPrimeiro pensamento da língua:")

evento = criar_evento()

print(evento)


frase = organizar_frase(evento)

print("\nFrase na língua:")

print(traduzir_frase(frase))