import numpy as np


def matrizJacobiBaseadaNoElemento_ij_DeRvelha(A, i, j):
    n = A.shape[0]
    theta = 0
    e = 1e-6
    J_ij = np.eye(n)
    if np.abs(A[i, j]) <= e:
        return J_ij
    if np.abs(A[j, j]) <= e:
        if A[i, j] < 0:
            theta = np.pi / 2
        else:
            theta = -(np.pi / 2)
    else:
        theta = np.arctan(-(A[i, j]) / A[j, j])

    J_ij[i, i] = np.cos(theta)
    J_ij[j, j] = np.cos(theta)
    J_ij[i, j] = np.sin(theta)
    J_ij[j, i] = -(np.sin(theta))

    return J_ij


def decomposicaoQR(A):
    n = A.shape[0]
    QT = np.eye(n)
    R_old = A.copy()
    for j in range(n - 1):
        for i in range(j + 1, n):
            J_ij = matrizJacobiBaseadaNoElemento_ij_DeRvelha(R_old, i, j)
            R_new = np.dot(J_ij, R_old)
            R_old = R_new.copy()
            QT = np.dot(J_ij, QT)
    Q = QT.T  # transposta
    R = R_new
    return Q, R


def printQR(Q, R, iter):
    print(60 * "=")
    print(f"Iteração {iter}")
    print("Q = \n", Q)
    print("\nR = \n", R)
    print(60 * "=")


def soma_dos_quadrados(A):
    abaixo_diagonal = A[np.tril_indices(len(A), -1)]  # elementos abaixo da diagonal
    abaixo_diagonal_quadrado = abaixo_diagonal**2
    soma = np.sum(abaixo_diagonal_quadrado)
    return soma


def metodoQR(A, e):
    n = A.shape[0]
    val = 100
    P = np.eye(n)
    A_old = A.copy()
    i = 1
    while val > e:
        Q, R = decomposicaoQR(A_old)
        printQR(Q, R, i)
        A_new = np.dot(R, Q)
        A_old = A_new.copy()
        P = np.dot(P, Q)
        val = soma_dos_quadrados(A_new)
        i += 1

    lamb = np.diagonal(A_new)

    return P, lamb


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

P, diag = metodoQR(A=A, e=epsilon)
print()

for i in range(P.shape[0]):
    print(f"({diag[i]:.5f}, {np.round(P[:,i], 5)})")
