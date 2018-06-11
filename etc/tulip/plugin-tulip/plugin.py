from tulip import tlp
import tulipplugins

class EigencentralityAlgorithm(tlp.DoubleAlgorithm):
    def __init__(self, context):
        tlp.DoubleAlgorithm.__init__(self, context)
        self.addFloatParameter(
            'lambda',
            help='Lambda constant',
            defaultValue='0.5')

    def check(self):
        return (True, "Ok")

    def run(self):
        result = self.dataSet['result']        
        lambdaProperty = float(self.dataSet['lambda'])
        centralities = self.calculateCentrality(self.graph, lambdaProperty)

        for node in self.graph.getNodes():
            result[node] = centralities[node]
        
        return True

    def calculateCentrality(self, V, l):
        """Calculates the eigenvector centrality on the Tulip graph `V` based
        on the required lambda constant, given by `l`."""
        # TODO Calculate the real eigenvector centrality for each node
        ds = { v: V.deg(v) for v in V.getNodes() }
        ec = { v: sum(map(lambda w: ds[w], V.getInOutNodes(v))) for v in V.getNodes() }
        return ec

# The line below does the magic to register the plugin to the plugin database
# and updates the GUI to make it accessible through the menus.
tulipplugins.registerPluginOfGroup(
    "EigencentralityAlgorithm", 
    "Eigenvector Centrality", 
    "Cristiano Silva Jr. <cristianoalvesjr@gmail.com>", 
    "30/01/2018", 
    "No info yet.", 
    "0.2", 
    "Python")
