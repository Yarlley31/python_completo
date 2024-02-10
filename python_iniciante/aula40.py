""" Calculadora com while """
while True:
    # Variáveis
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operator = input('Digite o operador (+-*/): ')

    num1_float = 0
    num2_float = 0
    
    numeros_validos = None
    operator_permitidos = '+-*/'
    # Calculadora
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números não são válidos.')
        continue
    
    if operator not in operator_permitidos:
        print('Operador inválido')
    if len(operator) > 1:
        print('Digite apenas um operador.')
        continue
    
    # Somatorio e resultado
    print('Realizando a conta. Confira o resultado abaixo:')
    print('-' * 12)
    if operator == '+':
        print(num1_float + num2_float)
    elif operator == '-':
        print(num1_float - num2_float)
    elif operator == '*':
        print(num1_float * num2_float)
    elif operator == '/':
        print(num1_float / num2_float)
    else:
        print('Você não deveria ver isso.')
    print('-' * 12)
    
    # Porta de saída
    sair = input('Quer sair? [s]im: ').upper().startswith('S')
    if sair is True:
        break