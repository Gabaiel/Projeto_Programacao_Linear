


####################### # O lontra disse que tem que aparecer essas mensagens de input para a Kelly


#m, n = list(map(int, list(input("Digite o número de linhas e de colunas separadas por um espaço, respectivamente: ").split(" ")))) # Números de restrições (linhas) e variáveis (colunas)
#c = list(map(int, list(input("Digite os custos separados por um espaço: ").split(" ")))) # Vetor dos custos
#b = list(map(int, list(input("Digite os termos independentes separados por um espaço: ").split(" ")))) # Vetor dos recursos
#A = [] # Matriz dos coeficientes das restrições
#M = max(list(map(abs, c))) * 1000 # Big-M
#
#for i in range(0, m):
#    row = list(map(int, list(input(f'Digite a linha {i+1} da matriz A: ').split(" "))))
#    A.append(row)

import numpy as np

m, n = list(map(int, list(input().split(" ")))) # Números de restrições (linhas) e variáveis (colunas)
c = list(map(int, list(input().split(" ")))) # Vetor dos custos
b = list(map(int, list(input().split(" ")))) # Vetor dos recursos
A = [] # Matriz dos coeficientes das restrições
M = max(list(map(abs, c))) * 1000 # Big-M

for i in range(0, m):
    row = list(map(int, list(input().split(" "))))
    A.append(row)

A = list(np.transpose(A))

   ## Aplicando o Big-M
   #for i in range(m):
   #    s = np.zeros(m)
   #    s[i] = 1
   #    A.append(list(s))
   #    c.append(M)

   #n += m

A = list(np.transpose(A))

# Fase I: partição básica inicial factível
B = [] # Matriz básica
N = [] # Matriz não-básica
c_b = c[n-m:] # Custo básico
c_n = c[:n-m] # Custo não-básico

# Determinando a partição básica factível

for i in range(0,len(A)) :
    B.append(A[i][n-m:])
    N.append(A[i][:n-m])

STOP = False
solucao_otima = False

# Fase II: 
while not STOP:
    print("Iteração")
    # Passo 1: calculando a solução básica
    x_b = np.linalg.solve(B, b)

    B = list(np.transpose(B))

    # Passo 2.1: Calculando o vetor multiplicador simplex
    Lambda = np.linalg.solve(B, c_b)
    
    B = list(np.transpose(B))

    Lambda = list(np.transpose(Lambda))

    # Passo 2.2: # Calculando os custos reduzidos das variáveis não-básicas
    c_n_r = [] # Vetor dos custos reduzidos
    c_n_r_index = []
    A = list(np.transpose(A))

    for j in range(len(c_n)):
        c_n_r.append(c_n[j] - np.matmul(Lambda, A[j]))
        c_n_r_index.append(j)

    C_n = min(c_n_r) 
    k = c_n_r.index(C_n) # Índice da variável que entra na base
    ############################################################# é possível nao salvar k aqui e no for acima e apenas salvar A[k] para usar no passo 4?

        # A[k] entra na base

    # Passo 3: Teste de Otimalidade
    print("Custos reduzidos:", C_n)
    if C_n >= 0:
        STOP = True
        solucao_otima = True
        #   print("A solução ótima do PPL é:", x_b)
        #   print("O valor ótimo do PPL é:", np.dot(c_b, x_b))
        break

    # Passo 4: Calculando a direção simplex
    a_k = list(np.transpose(A[k]))
    N = list(np.transpose(N))

    for idx, n in enumerate(N):
        if np.array_equal(n, A[k]):
            k = idx  # Índice da variável que entra na base

    y = np.linalg.solve(B, a_k)

    # Passo 5: Calculo do tamanho do passo
    e = []
    e_index = []
    if max(y) <= 0:
        STOP = True
        solucao_otima = False
        #   print("O problema é ilimitado.")
        break
    else:
        for l in range(len(x_b)):
            if y[l] > 0:
                e.append(x_b[l]/y[l])
                e_index.append(l)

    e_min = min(e)
    l = e_index[e.index(e_min)] # Índice da variável que sai da base
    
        # B[l] sai da base

    # Armazenando as variáveis e custos que entram e saem da base
    A_b = B[l]
    A_c_b = c_b[l]
    A_n = N[k]
    A_c_n = c_n[k]

    # Passo 6: Atualização da base
    for i in B:
        if np.array_equal(i, A_b):
            B[l] = A_n
            c_b[l] = A_c_n
            N[k] = A_b
            c_n[k] = A_c_b

    idx_b = idx_n = None

    for i, col in enumerate(A):
        if np.array_equal(col, A_b):
            idx_b = i
        if np.array_equal(col, A_n):
            idx_n = i

    if idx_b is not None and idx_n is not None:
        A[idx_b], A[idx_n] = A[idx_n], A[idx_b]
            
    A = list(np.transpose(A))
    print(B,N,c_b,c_n,sep="\n \n")

# Resposta final
if solucao_otima == True:
    print("A solução ótima do PPL é:", x_b)
    print("O valor ótimo do PPL é:", np.dot(c_b, x_b))
elif solucao_otima == False:
    print("O problema é ilimitado.")

#################### O print deve estar no final (fora do loop) ou dentro do loop?