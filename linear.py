import copy

def _deter(m):
    return (
    (m[0][0] * m[1][1] * m[2][2]) + 
    (m[0][1] * m[1][2] * m[2][0]) +
    (m[0][2] * m[1][0] * m[2][1]) -
    (m[0][2] * m[1][1] * m[2][0]) - 
    (m[0][0] * m[1][2] * m[2][1]) - 
    (m[0][1] * m[1][0] * m[2][2])
    )

def _change(m, c, p):
    m = copy.deepcopy(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j == p:
                m[i][j] = c[i]
    return m

def linear(m, c):
    d = _deter(m)
    if d == 0:
        raise Exception('Singular matrix')
    d1 = _deter(_change(m, c, 0))
    d2 = _deter(_change(m, c, 1))
    d3 = _deter(_change(m, c, 2))
    return [d1 / d, d2 / d, d3 / d]

__all__ = [
    'linear'
]