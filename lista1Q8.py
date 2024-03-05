# Garante que o ano seja um número inteiro
while True:
    try:
        a = int(input('Qual o ano a ser verificado se é bissexto? '))
    except Exception:
        print('Digite um ano válido!')
    else:
        break

# Verifica se o ano é bissexto ou não. Em seguida, exibe o resultado.
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
    print(f'O ano {a} é bissexto.')
else:
    print(f'O ano {a} não é bissexto.')
    