# Entradas:
#  m: n ́umero de restri ̧c ̃oes (linhas);
#  n: n ́umero de vari ́aveis (colunas);
#  c: vetor dos custos;
#  b: vetor dos recursos (ou termos independentes);
#  A: matriz dos coeficientes das restri ̧c ̃oes.
# 
# Sa ́ıdas:
#  Se o problema for ilimitado, exibir essa informa ̧c ̃ao.
#  Se o problema tiver solu ̧c ̃ao, exibir:
# • x: vetor das vari ́aveis de decis ̃ao, que  ́e a solu ̧c ̃ao  ́otima do PPL;
# • f(x): valor  ́otimo da solu ̧c ̃ao.

import numpy as np

m, n = list(map(int, list(input().split(" "))))
c = list(map(int, list(input().split(" "))))
b = list(map(int, list(input().split(" "))))
A = []
M = max(list(map(abs, c))) * 1000

for i in range(0, m):
    row = list(map(int, list(input().split(" "))))
    A.append(row)

A = list(np.transpose(A))

# Big-M
#for i in range(m):
#    s = np.zeros(m)
#    s[i] = 1
#    A.append(list(s))
#    c.append(M)
    

A = list(np.transpose(A))


B = []
N = []
c_b = c[:m]
c_n = c[n-m+1:]

# Determinar a partição básica factível

for i in range(0,len(A)) :
    B.append(A[i][:m])
    N.append(A[i][n-m+1:])

STOP = False
solucao_otima = False

x_b = np.linalg.solve(B, b)

B = list(np.transpose(B))

Lambda = np.linalg.solve(B, c_b)

B = list(np.transpose(B))

Lambda = list(np.transpose(Lambda))

c_chapeu_n = []
c_chapeu_index = []
A = np.transpose(A)
for j in range(len(c_n)):
    i = j + 1
    c_chapeu_n.append(c[j] - np.matmul(Lambda, A[i]))
    c_chapeu_index.append(i)

C_n = min(c_chapeu_n)
k = c_chapeu_index[c_chapeu_n.index(C_n)]

# A[i] entra na base
# Whilelalizar
if C_n >= 0:
    STOP = True
    solucao_otima = True

y = np.linalg.solve(B, A[k])

e = []
e_index = []
if max(y) <= 0:
    STOP = True
    solucao_otima = False
else:
    for l in range(len(x_b)):
        if y[l] > 0:
            e.append(x_b[l]/y[l])
            e_index.append(l)

e_min = min(e)
l = e_index[e.index(e_min)]

# my_array[:, [0, 1]] = my_array[:, [1, 0]]

print(np.transpose(A))
# print(np.tranpose(B))