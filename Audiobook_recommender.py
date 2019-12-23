from random import random
from random import randint


def dot_product(A, B):
    result = []
    if not isinstance(A[0], list):
        s = 0
        if len(A) != len(B):
            print('The sizes are not matched')
            return
        for i in range(len(A)):
            s += A[i] * B[i]
        return s

    else:
        if len(A[0]) != len(B[0]):
            print('The sizes are not matched')
            return
        for i in range(len(A)):
            temp = []
            for j in range(len(B)):
                s = 0
                for k in range(len(B[j])):
                    s = s + A[i][k] * B[j][k]
                temp.append(s)
            result.append(temp)
        if len(result[0]) == 1:
            return result[0][0]
        else:
            return result


def matrix_factorization(R, P, Q, K, steps=300, alpha=0.0002, beta=0.02):
    L = list(R)
    for step in range(steps):
        for step2 in range(len(L)):
            i = L[step2][0]
            j = L[step2][1]
            eij = R[(i, j)] - dot_product(P[i], Q[j])
            for k in range(K):
                P[i][k] = P[i][k] + alpha * (2 * eij * Q[j][k] - beta * P[i][k])
                Q[j][k] = Q[j][k] + alpha * (2 * eij * P[i][k] - beta * Q[j][k])

    return P, Q


###############################################################################

if __name__ == "__main__":
    R = {}
    number_of_votes, users, movies = map(int, input().split("\t"))

    for i in range(number_of_votes):
        user_id, movie_id, rating = map(int, input().split("\t"))
        R[(user_id, movie_id)] = rating

    K = 5

    P = []
    Q = []
    for i in range(users):
        temp = []
        for j in range(K):
            temp.append(random())
        P.append(temp)

    for i in range(movies):
        temp = []
        for j in range(K):
            temp.append(random())
        Q.append(temp)

    nP, nQ = matrix_factorization(R, P, Q, K)
    nR = dot_product(nP, nQ)

    for i in range(len(nR)):
        temp = []
        for j in range(len(nR[i])):
            if not ((i, j) in R):
                temp.append((nR[i][j], j))
        temp = sorted(temp, reverse=True, key=lambda x: x[0])
        for k in range(0, 9):
            print(temp[k][1], end = '\t')
        print(temp[9][1], end='\n')
