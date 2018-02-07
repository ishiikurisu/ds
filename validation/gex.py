import unicodedata
import sys
import codecs
import re

SOBRE = """
Este script foi copiado do arquivo `gerador_gexf`.
"""

# -----------------------------------------------------------------------------

"""
    Modulo responsavel pela exportacao dos registros de similaridade para um arquivo XML no formato GEXF.
"""

def export_gexf(rotulos,similaridades,nome_arquivo,threshold,excluir_negativos):

    """
        Exporta os registros de similaridade para o arquivo.

        Parametros:
        ----------

            rotulos: titulos dos documentos
            similaridade: tabela de similaridade
            nome_arquivo: nome do arquivo para o qual os registros de similaridade serao exportados
            threshold: valor minimo de similaridade para que um registro seja incluido
            excluir_negativos: true - registros com similaridade negativa nao sao incluidos

    """

    tbl = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))

    arquivo = codecs.open(nome_arquivo + ".gexf","w","utf-8")
    arquivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    arquivo.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
    arquivo.write('\t<graph mode="static" defaultedgetype="undirected">\n')
    arquivo.write('\t\t\t<nodes>\n')
    arquivo.flush()

    cont=0
    docs = list(rotulos.keys())
    for key in docs:
        rotulo = re.sub(r'[<>]', '', rotulos[key].translate(tbl))
        arquivo.write(u"\t\t\t\t<node id=\"%d\" label=\"%s\"/>\n" % (docs.index(key), rotulo))

        cont = cont+1
        if cont == 50:
            arquivo.flush()
            cont = 0

    arquivo.write('\t\t\t</nodes>\n')
    arquivo.write('\t\t\t<edges>\n')
    arquivo.flush()

    cont=0
    for similaridade in similaridades:
        if(excluir_negativos and (similaridade[2] < 0)):
            continue

        if abs(similaridade[2]) >= threshold:
            arquivo.write("\t\t\t\t<edge source=\"%d\" target=\"%d\" weight=\"%f\" />\n" % (docs.index(similaridade[0]),docs.index(similaridade[1]),similaridade[2]))

        cont = cont+1
        if cont == 50:
            arquivo.flush()
            cont = 0

    arquivo.write('\t\t\t</edges>\n')
    arquivo.write('\t</graph>\n')
    arquivo.write('</gexf>')
    arquivo.close() # you can omit in most cases as the destructor will call it

def export_gexf_termos(rotulos,similaridades,nome_arquivo,threshold,excluir_negativos):

    """
        Exporta os registros de similaridade para o arquivo.

        Parametros:
        ----------

            rotulos: titulos dos documentos
            similaridade: tabela de similaridade
            nome_arquivo: nome do arquivo para o qual os registros de similaridade serao exportados
            threshold: valor minimo de similaridade para que um registro seja incluido
            excluir_negativos: true - registros com similaridade negativa nao sao incluidos

    """

    tbl = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))

    arquivo = codecs.open(nome_arquivo + ".gexf","w","utf-8")
    arquivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    arquivo.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
    arquivo.write('\t<graph mode="static" defaultedgetype="undirected">\n')
    arquivo.write('\t\t\t<nodes>\n')
    arquivo.flush()

    cont=0
    cont2=0;
    for key in rotulos:
        arquivo.write(u"\t\t\t\t<node id=\"%d\" label=\"%s\"/>\n" % (cont2,key))
        cont = cont+1
        cont2 = cont2+1
        if cont == 50:
            arquivo.flush()
            cont = 0

    arquivo.write('\t\t\t</nodes>\n')
    arquivo.write('\t\t\t<edges>\n')
    arquivo.flush()

    cont=0
    for similaridade in similaridades:
        if(excluir_negativos and (similaridade[2] < 0)):
            continue

        if abs(similaridade[2]) >= threshold:
            label = ' - '.join((similaridade[0],similaridade[1]))
            arquivo.write("\t\t\t\t<edge source=\"%d\" target=\"%d\" weight=\"%f\" label=\"%s\" />\n" % (rotulos.index(similaridade[0]),rotulos.index(similaridade[1]),similaridade[2],label))

        cont = cont+1
        if cont == 50:
            arquivo.flush()
            cont = 0

    arquivo.write('\t\t\t</edges>\n')
    arquivo.write('\t</graph>\n')
    arquivo.write('</gexf>')
    arquivo.close() # you can omit in most cases as the destructor will call it
