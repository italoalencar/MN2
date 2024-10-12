import numpy as np
import potencia_inversa


def potencia_shifter(A, v0, u, e):
    n = A.shape[0]
    I = np.eye(n)
    A_new = A - np.dot(u, I)
    lambda_menor, x_n = potencia_inversa(A_new, v0, e)
    lambda_n = lambda_menor + u
    return lambda_n, x_n


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

autovalor, autovetor = potencia_shifter(A=A, v0=v0, u=5, e=epsilon)
print(f"Potencia com Deslocamento:\nAutovalor: {autovalor}\nAutovetor: {autovetor}")
