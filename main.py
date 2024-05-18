# entrada de dados
nome = input('Informe seu nome: ')
peso = str(input('Informe seu peso em kg: '))
altura = str(input('Informe sua altura em metros: '))

peso = peso.replace(',', '.')
altura = altura.replace(',', '.')

try:
    # converte para float
    peso = float(peso)
    altura = float(altura)

    # calcula o imc
    imc = peso/(altura**2)

    # exibe o resultado do imc
    print(f'O valor do IMC de {nome} é {imc:,.2f}.')

    # verifica a saúde do usuário
    if imc < 17:
        print(f'{nome} está muito abaixo do peso.')
    elif imc < 18.5:
        print(f'{nome} está abaixo do peso.')
    elif imc < 25:
        print(f'{nome} está no seu peso ideal.')
    elif imc < 30:
        print(f'{nome} está acima do peso.')
    elif imc < 35:
        print(f'{nome} está obeso.')
    elif imc < 40:
        print(f'{nome} está com obesidade grau II.')
    else:
        print(f'{nome} está com obesidade mórbida.')
except:
    print('Não foi possível calcular o IMC.')