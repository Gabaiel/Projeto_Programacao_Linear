#m, n = list(map(int, list(input("Digite o número de linhas e de colunas separadas por um espaço, respectivamente: ").split(" ")))) # Números de restrições (linhas) e variáveis (colunas)
#c = list(map(int, list(input("Digite os custos separados por um espaço: ").split(" ")))) # Vetor dos custos
#b = list(map(int, list(input("Digite os termos independentes separados por um espaço: ").split(" ")))) # Vetor dos recursos
#A = [] # Matriz dos coeficientes das restrições
#M = max(list(map(abs, c))) * 1000 # Big-M
#
#for i in range(0, m):
#    row = list(map(int, list(input(f'Digite a linha {i+1} da matriz A: ').split(" "))))
#    A.append(row)

i=0

while i<5:
    print(i)
    i+=1
    if i==3:
        break
    print(i*10)