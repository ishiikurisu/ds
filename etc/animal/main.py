import json

def load(filename):
    outlet = None
    with open(filename, 'r') as fp:
        outlet = json.loads(fp.read())
    return outlet

def brandes2dolphins(V):
    cb = { v: 0 for v in V.keys() }
    for s in V.keys():
        S = []
        Q = [s]
        sig = { s: 1 }
        d = { t: -1 if t != s else 0 for t in V.keys() } 
        ps = { w: [] for w in V.keys() }
        for t in V.keys():
            if t is not s:
                sig[t] = 0
                d[t] = -1
        while len(Q) > 0:
            v = Q[0]
            del Q[0]
            S.append(v)     
            W = V[v]['ties']
            for w in W:
                if d[w] < 0:
                    Q.append(w)
                    d[w] = d[v] + 1
                if d[w] is d[v]+1:
                    sig[w] += sig[v]
                    ps[w].append(v)
        delta = { v: 0 for v in V.keys() }
        # S returns vertices in order of non-increasing distance from s        
        while len(S) > 0:
            w = S.pop()
            for v in ps[w]:
                delta[v] += (sig[v]/sig[w])*(1+delta[w])
            if w is not s:
                cb[w] += delta[w]
    return cb

def calculate_centrality(cb):
    return max(map(lambda v: (v, cb[v]), cb.keys()), key=lambda p: p[1])[0]

if __name__ == '__main__':
    dolphins = load('dolphin.json')
    betweenness = brandes2dolphins(dolphins)
    central = calculate_centrality(betweenness)
    print(betweenness, central)
    print('the central dolphin is %s' % (dolphins[central]['gender']))