import sys
from tulip import tlp
from tulipgui import tlpgui

def load_csv_to_tulip(csvfilename):
    graph = None

    with open(csvfilename, 'r') as fp:
        graph = tlp.newGraph()
        nodes = []
        line_no = 0

        for line in fp:
            if line_no == 0:
                ids = map(lambda s: s.strip(), filter(lambda s: len(s) > 0, line.strip().split(';')))
                for node_id in ids:
                    node = graph.addNode({
                        'name': node_id
                    })
                    nodes.append(node)
            else:
                fields = list(map(lambda s: s.strip(), line.split(';')))
                edges = map(lambda s: float(s.strip()), filter(lambda s: len(s) > 0, fields[1:]))
                source = nodes[line_no-1]
                for col_no, edge in enumerate(edges):
                    if edge > 0:
                        target = nodes[col_no-1]
                        graph.addEdge(source, target)
            line_no += 1

    return graph


def coloring_nodes(graph):
    """This is an example algorithm that colors nodes depending on their degree"""
    blue = tlp.Color(0,0,255)
    green = tlp.Color(0,255,0)
    viewColor = graph.getColorProperty("viewColor")
    viewMetric = graph.getDoubleProperty("viewMetric")

    params = tlp.getDefaultPluginParameters('Betweenness Centrality', graph)
    success, about = graph.applyDoubleAlgorithm('Betweenness Centrality', params)
    if success:
        for n in graph.getNodes():
            betweenness = viewMetric[n]
            if betweenness > 10:
                viewColor[n] = blue
            else:
                viewColor[n] = green
    else:
        print(about)
        return


def save_graph(graph, outputname):
    tlp.saveGraph(graph, outputname)

if __name__ == '__main__':
    print('# Indie Tulip')
    print('loading data...')
    graph = load_csv_to_tulip(sys.argv[1])
    print('studying data...')
    coloring_nodes(graph)
    print('saving results...')
    save_graph(graph, sys.argv[2])
