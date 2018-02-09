import sys
import mat
import sim
import time
import gex

def calcular_lsa(conjunto):
    """
    Realiza a análise semêntica de um conjunto de documentos. `conjunto` deve ser o caminho para
    uma tabela CSV contendo 4 campos (Label, DOI, Abstract, & Published in). Salva um arquivo
    Gephi contendo as mesmas análises realizadas no teste original de validação do artigo.
    """
    # Pré-Processamento
    # =================
    documentos = carregar_documentos(conjunto)
    docs = list(documentos.keys()) # para brevidade
    matriz_tf, termos = mat.construir_matriz_TF(documentos)
    tfidf = mat.calcular_TfIdf(matriz_tf)

    # Analisando documentos
    # =====================
    U, S, Vt = mat.svd(tfidf)
    matriz_documento_documento, _, _ = sim.calcular_similaridade_documentos(U, S, Vt, len(docs))
    similaridades = sim.obter_similaridades(docs, matriz_documento_documento)
    gex.export_gexf(documentos, similaridades, nomear_saida(conjunto, 'doc'), 0, False)

    # Analisando termos
    # =================
    U, S, Vt = mat.svd(tfidf.T)
    matriz_termo_termo, _, _ = sim.calcular_similaridade_documentos(U, S, Vt, len(termos))
    similaridades = sim.obter_similaridades(termos, matriz_termo_termo)
    gex.export_gexf_termos(termos, similaridades, nomear_saida(conjunto, 'termo'), 0, False)

    # Salvando outros dados relevantes
    # ================================
    with open('tf.csv', 'w') as fp:
        fp.write(gerar_csv(termos, docs, matriz_tf))

#################
# ENTRADA/SAÍDA #
#################

def carregar_documentos(entrada):
    """
    Carrega um arquivo CSV no formato especificado pelo teste em um dicionário onde cada chave é o
    título de um artigo e o seu valor associado é o _abstract_ deste artigo. Essa seção é
    originalmente realizada com uma consulta ao banco de dados. Neste caso, será necessário abrir e
    processar o arquivo na mão.
    """
    saida = {}

    with open(entrada, 'r') as fp:
        no_linha = 0
        for linha in fp:
            if no_linha > 0:
                try:
                    campos = linha.strip().split('\t')
                    saida[campos[0]] = campos[2]
                except IndexError:
                    print('linha {0} corrompida!'.format(no_linha+1))
            no_linha += 1

    return saida

def gerar_csv(cols, lins, m):
    """
    Salva a matriz `m` em um arquivo CSV onde as colunas são identificadas por `cols` e as linhas,
    por `lins`.
    """
    saida = ';{0}\n'.format(';'.join(cols))

    for y, lin in enumerate(lins):
        saida += '{0};{1}\n'.format(lin, ';'.join(map(lambda v: '%.4f' % (v), m[:, y])))

    return saida

def nomear_saida(entrada, caracteristica):
    return '{0}-{1}'.format('.'.join(entrada.split('.')[0:-1]), caracteristica)

if __name__ == '__main__':
    then = time.time()
    entrada = sys.argv[1]
    calcular_lsa(entrada)
    now = time.time()
    print("%.2fs" % (now - then))
