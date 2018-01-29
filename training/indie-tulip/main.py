import sys
from tulip import tlp

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

    if graph is not None:
        for n in graph.getNodes():
            print(n)
        for e in graph.getEdges():
            print(e)

    return graph

if __name__ == '__main__':
    print('# Indie Tulip')
    graph = load_csv_to_tulip(sys.argv[1])
    # TODO Save file as a tulip file
    # TODO Analyze graph and genererate a plot with Tulip
