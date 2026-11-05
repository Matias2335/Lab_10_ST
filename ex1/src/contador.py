def contar_palavras(texto):
    return {}

def contar_palavras(texto):
    if texto == "":
        return {}
    return {texto: 1}

def contar_palavras(texto):
    contagem = {}
    for palavra in texto.split():
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

def contar_palavras(texto):
    contagem = {}
    for palavra in texto.split():
        palavra = palavra.lower()
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

def contar_palavras(texto):
    contagem = {}
    for palavra in texto.split():
        palavra = palavra.lower().strip(".,;:!?")
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem