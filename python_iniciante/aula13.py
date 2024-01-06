nome = 'Yarlley Fernandes'
altura = 1.70
peso = 52
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Yarlley Fernandes tem 1.70 de altura,
# pesa 52 quilos e seu IMC é
# 17.99307958477509