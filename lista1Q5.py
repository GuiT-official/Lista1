# Cria a lista a ser armazenados os valores dos lados do triângulo.
a = []

# Cria uma classe para organizar as funções responsáveis por cada requisição de cada lado do triângulo, ao usuário.
class Lados:
    def l1():
        # Garante que o lado 1 tenha valor numérico e positivo.
        while True:
            try:
                b = float(input('Qual o tamanho do 1º lado do triângulo? (apenas o valor numérico) '))
                if negativo(b):
                    print('Digite um número válido!')
                    continue
            except Exception:
                print('Digite um número válido!')
            else:
                a.append(b)
                break
    def l2():
        # Garante que o lado 2 tenha valor numérico e positivo.
        while True:
            try:
                b = float(input('Qual o tamanho do 2º lado do triângulo? (apenas o valor numérico) '))
                if negativo(b):
                    print('Digite um número válido!')
                    continue
            except Exception:
                print('Digite um número válido!')
            else:
                a.append(b)
                break
    def l3():
        # Garante que o lado 3 tenha valor numérico e positivo.
        while True:
            try:
                b = float(input('Qual o tamanho do 3º lado do triângulo? (apenas o valor numérico) '))
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
        c = 'escaleno'
    if b == 5: # b possuirá valor de 5, caso o triângulo seja isóceles, pois haverão apenas 2 valores iguais (2+2+1).
        c = 'isóceles'
    if b == 9: # b possuirá valor de 9, caso o triângulo seja equilátero, pois todos os valores serão iguais entre si (3+3+3).
        c = 'equilátero'
    return c

# Função para verificar se um número é negativo.
def negativo(x):
    if x/abs(x) == -1.0:
        return True

# Função de cálculo da área do triângulo
def calculo():
    s = (a[0]+a[1]+a[2])/2
    return (s*(s-a[0])*(s-a[1])*(s-a[2]))**(1/2)

Lados.l1()
Lados.l2()
Lados.l3()

print(f'O tipo do triângulo é {verificar_tipo()}.') # Exibe o tipo do triângulo
print(f'A área do triângulo é {calculo()} u.a.') # Exibe a área do triângulo
