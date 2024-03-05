# Garante que o sexo seja masculino ou feminino. (M, F, m ou f)
while True:
    a = input('Qual o sexo do indivíduo a ser consultado?(M/F) ').upper()
    if a in ('M','F'):
        break
    print('Digite um caractere válido!')

# Garante que a idade seja um número inteiro.
while True:
    try:
        b = int(input('Qual a idade dele? '))
    except Exception:
        print('Digite uma idade válida!')
    else:
        break

# Garante que o tempo de contribuição seja um número inteiro.
while True:
    try:
        c = int(input('Qual o tempo de contribuição do mesmo? '))
    except Exception:
        print('Digite um tempo de contribuição válido!')
    else:
        break

def aposenta(): # Função que exibe o resultado para o caso de confirmação da aposentadoria.
    print('Aposentável')
def naposenta(): # Função que exibe o resultado para o caso de negação da aposentadoria.
    print('Não Aposentável')

if a == 'M' and ((b >= 65 and c >= 10) or (b >= 63 and c >= 15)): # Verifica os critérios de aposentadoria, sob a condição do indivíduo ser do sexo masculino.
    aposenta()
elif a == 'F' and ((b >= 63 and c >= 10) or (b >= 61 and c >= 15)): # Verifica os critérios de aposentadoria, sob a condição do indivíduo ser do sexo feminino.
    aposenta()
else:
    naposenta()
