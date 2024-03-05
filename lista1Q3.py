# Garante que o número seja realmente um número racional.
while True:
    try:
        a = float(input('Qual o número racional para o cálculo da função? '))
    except Exception:
        print('Digite um número válido!')
    else:
        break

# Exibe o resultado do cálculo.
print(a**(1/2)+a/2+a**a)