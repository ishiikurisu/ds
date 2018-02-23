class Promethee:
    def __init__(self, actions, criteria):
        """
        Creates a new PROMETHEE tool for analyzing a set of actions and
        criteria.
        """
        self.actions = actions
        self.criteria = criteria
        self.weights = [i+1 for i, _ in enumerate(criteria)]

    def set_weights(self, weights):
        """
        Defines new weights for this Promethee tool.
        """
        print(weights)
        self.weights = weights

    def recommend(self, table):
        """
        Based on the previously set actions, criteria, and weights, chooses
        the best option using the ranking table.
        """
        # TODO Implement me!
        outlet = []
        outlet = self.actions
        return outlet

def roc(ranking):
    """
    Creates a ROC ranking from a ranking
    """
    n = len(ranking)
    def w(j):
        return sum([1/k for k in range(j, n+1)])/n
    return [w(j) for j in ranking]
