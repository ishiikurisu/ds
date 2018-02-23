import numpy as np

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
        self.weights = weights

    def recommend(self, table):
        """
        Based on the previously set actions, criteria, and weights, chooses
        the best option using the ranking table.
        `table` must be a matrix with `len(actions)` x `len(criteria)`
        dimensions.
        """
        outlet = []
        outlet = self.actions

        # Calculating preferences
        n = len(self.actions)
        prefs = np.zeros([n, n])
        for a, _ in enumerate(self.actions):
            for b, _ in enumerate(self.actions):
                p = 0
                for j in range(len(self.criteria)):
                    p += (table[a][j] - table[b][j]) * self.weights[j]
                prefs[a][b] = p

        # TODO Calculate flow
        return outlet

def roc(ranking):
    """
    Creates a ROC ranking from a ranking
    """
    n = len(ranking)
    def w(j):
        return sum([1/k for k in range(j, n+1)])/n
    return [w(j) for j in ranking]
