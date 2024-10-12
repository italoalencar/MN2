import numpy as np


def potencia_regular(A, v0, e):
    lambda_new = 0
    v_new = v0
    erro = 1000
    while erro > e:
        lambda_old = lambda_new
        v_old = v_new.copy()
        x1 = v_old / np.sqrt(np.dot(v_old.T, v_old))
        v_new = np.dot(A, x1)
        lambda_new = np.dot(x1.T, v_new)
        erro = np.abs((lambda_new - lambda_old) / lambda_new)

    return lambda_new, x1


A = np.array(
    [
        [4, -5, 4, -7, 2],
        [-5, -3, -8, 6, 1],
        [4, -8, 2, 0, -2],
        [-7, 6, 0, 8, -7],
        [2, 1, -2, -7, -2],
    ]
)

v0 = np.array([1, 1, 1, 1, 1])
epsilon = 1e-6

autovalor, autovetor = potencia_regular(A=A, v0=v0, e=epsilon)
print(f"Potencia Regular:\nAutovalor: {autovalor}\nAutovetor: {autovetor}\n")
