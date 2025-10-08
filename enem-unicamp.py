print("Calculadora de Média Ponderada do ENEM")
print("Por favor, insira abaixo a nota e peso, de acordo com a área de conhecimento, da seginte forma:")
print("760,9 1")
print("Insira os pesos como números inteiros de um dígito: _ 1")
print("Insira as notas como números decimais de 4 dígitos: 810,0")
print("LC - Linguagens e códigos", "MT - Matemática", "CN - Ciências da Natureza", "CH - Ciências Humanas", "RED - Redação", sep = '\n')

curso = input("Digite o curso escolhido: ")

LC = input("LC = ").split()
MT = input("MT = ").split()
CN = input("CN = ").split()
CH = input("CH = ").split()
RED = input("RED = ").split()

Média = 0
Peso = 0


for n in [LC,CH,CN,MT,RED]:
    for j in range(0,2):
        if "," in n[j]:
            n[j] = n[j].replace(",",".")
        n[j] = float(n[j])
    Média += n[0]*n[1]
    Peso += n[1]

    print(Média, Peso)

Média = round(Média/Peso, 1)

print("Sua média para ", curso, " é ", Média)