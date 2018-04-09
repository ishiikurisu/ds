"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    S = np.zeros_like(x)
    s = S.shape
    cases = 1
    if len(s) > 1:
        cases = s[1]

    if cases == 1:
        for i in range(s[0]):
            S[i] = np.exp(x[i]) / sum(np.exp(x))
    else:
        for j in range(cases):
            for i in range(s[0]):
                S[i,j] = np.exp(x[i,j]) / sum(np.exp(x[:,j]))

    return S

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
