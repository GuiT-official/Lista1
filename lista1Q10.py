# Garante que o 1º número seja racional.
while True:
    try:
        a = float(input('Qual o 1º número? '))
    except Exception:
        print('Digite um número válido!')
    else:
        break

# Garante que o 2º número seja racional.
while True:
    try:
        b = float(input('Qual o 2º número? '))
    except Exception:
        print('Digite um número válido!')
    else:
        break

# Garante que o operador seja +, -, * ou /.
while True:
    c = input('Qual o operador?("+", "-", "*" ou "/")')
    if c in ('+','-','*','/'):
        break
    print('Digite um operador válido!')

d = eval(f'{a}{c}{b}') # Une o 1º número com o operador e com o 2º número, nesta ordem, em forma de string. Em seguida, converte a string em uma expressão válida no python e obtém seu retorno.
print(f'Resultado de {a}{c}{b}: {d}') # Exibe o resultado.
