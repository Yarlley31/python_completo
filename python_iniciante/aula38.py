"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qnd_linhas = 5
qnd_colunas = 5

linha = 1
while linha <= qnd_linhas:
    coluna = 1
    while coluna <= qnd_colunas:
        coluna += 1
        print(f'{linha=}, {coluna=}')
    linha += 1

print("Acabou")