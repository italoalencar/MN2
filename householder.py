import numpy as np


def householder(A, i):
    n = A.shape[0]
    w = np.zeros(n)
    w_prime = np.zeros(n)
    e = np.zeros(n)

    w[i + 1 :] = A[i + 1 :, i]
    L_w = np.linalg.norm(w)
    w_prime[i + 1] = L_w
    N = w - w_prime
    N_norm = np.linalg.norm(N)
    if N_norm != 0:
        N = N / N_norm
    H = np.eye(n) - (2 * np.outer(N, N.T))

    return H


def metodoHouseholder(A):
    n = A.shape[0]

    H = np.eye(n)
    A_anterior = A.copy()

    for i in range(n - 2):
        Hi = householder(A_anterior, i)
        A_i = Hi.T @ A_anterior @ Hi
        A_anterior = A_i
        H = H @ Hi

    A_tridiag = A_i
    return A_tridiag, H
