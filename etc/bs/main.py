import numpy as np
import matplotlib.pyplot as mpl

def U(t):
    return 1 if t > 0 else 0

def B(t, s):
    return U(t) - U(t-s)

if __name__ == '__main__':
    fs = 1/1024
    t = np.arange(-3, 3, fs)
    b2 = list(map(lambda x: B(x, 2), t))
    mpl.plot(t, b2)
    mpl.savefig('bs.png')
    mpl.clf()
