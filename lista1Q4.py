# Garante que o número x seja inteiro.
while True:
    try:
        x = int(input('Qual o valor inteiro de x? '))
    except Exception:
        print('Digite um número válido!')
    else:
        break

# Garante que o número y seja inteiro.
while True:
    try:
        y = int(input('Qual o valor inteiro de y? '))
    except Exception:
        print('Digite um número válido!')
    else:
        break

# Armazena os valores de x e y em uma lista em x. Em seguida, os distribui na ordem contrária.
x = [x,y]
y = x[0]
x = x[1]

# Exibe o resultado.
print('x:',x,' y:',y)
