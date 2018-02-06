import numpy as np
import nltk.data
import re
from nltk.tokenize import word_tokenize
import nltk.corpus
from scipy import linalg

#############################
# RECUPERAÇÃO DE INFORMAÇÃO #
#############################

def construir_matriz_TF(documentos, stemming=False):
    """
    Transforma o dicionário de documentos em uma matriz numpy termo-frequência e a lista de termos
    encontrados. Esses termos podem ser reduzidos à raiz caso se adicione o parâmetro booleano
    opcional _stemming_.
    """
    dicionario = {}
    dcount = 0

    for titulo in documentos.keys():
        documento = '{0} {1}'.format(titulo, documentos[titulo])
        palavras = extrair_palavras(documento, stemming)

        for palavra in palavras:
            if palavra in dicionario:
                dicionario[palavra].append(dcount)
            else:
                dicionario[palavra] = [dcount]
        dcount += 1

    termos = sorted(k for k in dicionario.keys())
    matriz = np.zeros([len(termos), dcount])

    for i, k in enumerate(termos):
        for d in dicionario[k]:
            matriz[i, d] += 1

    return matriz, termos

def extrair_palavras(documento, stemming):
    """
    Transforma um documento em uma lista de stems a serem utilizados por um processador semântico.
    O parâmetro `documento` deve ser uma string contendo um texto a ser utilizado. Caso se deseje
    reduzir os termos aos seus radicais, o parâmetro `stemming` deve ser verdadeiro; ou falso caso
    contrário.
    """
    # BUG The stemming variable is not being used
    termos = filter(lambda p: not eh_invalido(p), word_tokenize(re.sub(r'\-', ' ', documento)))
    palavras = list(map(lambda s: s.lower(), termos))

    return palavras

def eh_invalido(termo):
    """
    Indica se um termo em um texto é um stem válido ou não, ou seja, se não é stopword, alguma
    palavra proibida ou pontuação, por exemplo.
    """
    p = termo.lower()
    lista_de_exclusao = ['PRP','CC','IN','DT','WDT','IN','BER','MD','BE','TO', 'II']
    stopwords = nltk.corpus.stopwords.words('english')
    return (p in lista_de_exclusao) or (p in stopwords) or (re.match(r'[^\w]', p, re.UNICODE))

##########
# TF.IDF #
##########

def calcular_TfIdf(matriz_frequencias):
    """
    Copiada de `processador_linguistico`.
    """
    try:
        WordsPerDoc = np.sum(matriz_frequencias, axis=0)
        DocsPerWord = np.sum(np.asarray(matriz_frequencias > 0, 'i'), axis=1)
        rows, cols = matriz_frequencias.shape
        for i in range(rows):
            for j in range(cols):
                matriz_frequencias[i,j] = (matriz_frequencias[i,j] / WordsPerDoc[j]) * np.log(float(cols) / DocsPerWord[i])
        return(np.nan_to_num(matriz_frequencias))
    except Exception as message:
        print(message)

def svd(matriz_termo_documento):
    """
    Método que realiza a decomposicao matricial. Copiado de `lsa`.
    """
    U, S, Vt = linalg.svd(matriz_termo_documento, full_matrices=False)
    return U, S, Vt
