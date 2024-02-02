"""
Introdução ao try/except
try -> tentar execultar o código
except -> ocorreu algum erro ao tentar execultar
"""
numero_str = input("Vou dobrar o número que você digitar: ")
# Lembrar de sempre tratar o input do usuario

try:
    print("STR:", numero_str) 
    numero_float = float(numero_str) # caso o programa não consiga transformar a str em float ele vai pular direto pro except
    print("FLOAT", numero_float)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print("Isto não é um número")


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
# else:
#     print("Isto não é um número")