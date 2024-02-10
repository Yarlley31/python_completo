frase = 'O Python é uma linguagem de programção '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

# iterando string
i = 0
qntd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    qntd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if qntd_apareceu_mais_vezes < qntd_apareceu_mais_vezes_atual:
        qntd_apareceu_mais_vezes = qntd_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual
    
    i += 1
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais_vezes}" que apareceu '
    f'{qntd_apareceu_mais_vezes}x'
)
