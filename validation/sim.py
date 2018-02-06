import numpy as np
from sklearn.preprocessing import Normalizer

def calcular_similaridade_documentos(U, S, Vt, k):
    """
    Copiado de `lsa`.
    """
    #reduz as dimensoes de S (ainda um vetor unidimensional) mediante a atribuicao de zeros �s posicoes maiores do que 'k'
    S[k:] = 0

    #multiplica as matrizes, trunca (remove linhas zeradas) e transpoem a matriz resultante
    matriz_documento_conceito = np.dot(np.diag(S), Vt)[:k,].T
    similaridade = Normalizer(copy=False).fit_transform(matriz_documento_conceito)
    similaridade = np.dot(similaridade, similaridade.T)
    #S[2:] = 0

    #gera uma matriz termo-conceito de 2 dimensoes
    termo_conceito = np.dot(U, np.diag(S))
    #documento_conceito = np.dot(np.diag(S),Vt).T
    documento_conceito = np.dot(np.diag(S), Vt)

    return similaridade, termo_conceito, documento_conceito

def obter_similaridades(ids_documentos, matriz_similaridades):
    """
    Copiado de `lsa`.
    """
    similaridades = []

    for x in range(0 ,matriz_similaridades.shape[1]):
        for y in range(x+1, matriz_similaridades.shape[0]):
            similaridades.append((ids_documentos[x],ids_documentos[y],matriz_similaridades[x,y]))

    return similaridades
