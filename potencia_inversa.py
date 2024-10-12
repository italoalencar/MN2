import numpy as np
import potencia_regular


def potencia_inversa(A, v0, e):
    A_inv = np.linalg.inv(A)
    lambda_i, x1 = potencia_regular(A_inv, v0, e)
    lambda_n = 1 / lambda_i

    return lambda_n, x1


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

autovalor, autovetor = potencia_inversa(A=A, v0=v0, e=epsilon)
print(f"Potencia Inversa:\nAutovalor: {autovalor}\nAutovetor: {autovetor}\n")
