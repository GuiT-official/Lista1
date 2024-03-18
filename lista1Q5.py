# Cria a lista a ser armazenados os valores dos lados do triângulo.
a = []

# Garante que o lado c tenha valor numérico e positivo.
def Lados(c):
    while True:
        try:
            b = float(input(f'Qual o tamanho do {c}º lado do triângulo? (apenas o valor numérico) '))
            if negativo(b):
                print('Digite um número válido!')
                continue
        except Exception:
            print('Digite um número válido!')
        else:
            a.append(b)
            break

# Função para verificar o tipo do triângulo.
def verificar_tipo():
    b = 0
    for e in a:
        b += a.count(e)
    if b == 3: # b possuirá valor de 3, caso o triângulo seja escaleno, pois todos os valores serão diferentes entre si (1+1+1).
        return 'escaleno'
    if b == 5: # b possuirá valor de 5, caso o triângulo seja isóceles, pois haverão apenas 2 valores iguais (2+2+1).
        return 'isóceles'
    if b == 9: # b possuirá valor de 9, caso o triângulo seja equilátero, pois todos os valores serão iguais entre si (3+3+3).
        return 'equilátero'

# Função para verificar se um número é negativo.
def negativo(x):
    if x/abs(x) == -1.0:
        return True

# Função de cálculo da área do triângulo
def calculo():
    s = (a[0]+a[1]+a[2])/2
    return (s*(s-a[0])*(s-a[1])*(s-a[2]))**(1/2)

Lados(1)
Lados(2)
Lados(3)

print(f'O tipo do triângulo é {verificar_tipo()}.') # Exibe o tipo do triângulo
print(f'A área do triângulo é {calculo()} u.a.') # Exibe a área do triângulo
