# Garante que a unidade de temperatura seja em Fahrenheit ou Celsius. (inputs de F, C, f ou c)
while True:
    a = input('Qual a unidade de temperatura do valor que deseja converter?(F/C) ').upper()
    if a in ('F','C'):
        break
    print('Digite um caractere válido!')

# Garante que o valor de temperatura seja numérico
while True:
    try:
        b = float(input('Qual o valor númerico de temperatura? '))
    except Exception:
        print('Digite um valor válido!')
    else:
        break

# Verifica a unidade respectiva e converte o valor numérico associado para a unidade alternativa.
if a == 'F':
    print(f'O valor em Celsius é de: {(b-32)/1.8:.1f} °C')
else:
    print(f'O valor em Fahrenheit é de: {b*1.8+32:.1f} °F')
