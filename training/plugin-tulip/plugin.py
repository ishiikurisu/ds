from tulip import tlp
import tulipplugins

class EigencentralityAlgorithm(tlp.DoubleAlgorithm):
    def __init__(self, context):
        tlp.DoubleAlgorithm.__init__(self, context)
        # you can add parameters to the plugin here through the following syntax
        # self.add<Type>Parameter("<paramName>", "<paramDoc>", "<paramDefaultValue>")
        # (see documentation of class tlp.WithParameter to see what types of parameters are supported)

    def check(self):
        # This method is called before applying the algorithm on the input graph.
        # You can perform some precondition checks here.
        # See comments in the run method to know how to access to the input graph.

        # Must return a tuple (boolean, string). First member indicates if the algorithm can be applied
        # and the second one can be used to provide an error message
        return (True, "Ok")

    def run(self):
        # This method is the entry point of the algorithm when it is called
        # and must contain its implementation.

        # The graph on which the algorithm is applied can be accessed through
        # the "graph" class attribute (see documentation of class tlp.Graph).

        # The parameters provided by the user are stored in a dictionnary
        # that can be accessed through the "dataSet" class attribute.

        # The result of this measure algorithm must be stored in the
        # double property accessible through the "result" class attribute
        # (see documentation to know how to work with graph properties).

        # The method must return a boolean indicating if the algorithm
        # has been successfully applied on the input graph.
        return True

# The line below does the magic to register the plugin to the plugin database
# and updates the GUI to make it accessible through the menus.
tulipplugins.registerPluginOfGroup(
    "EigencentralityAlgorithm", 
    "Calculates the Eigencentrality of each node.", 
    "Cristiano Silva Jr. <cristianoalvesjr@gmail.com>", 
    "30/01/2018", 
    "No info yet.", 
    "0.1", 
    "Python")