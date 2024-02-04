print("Olá que horas são agora?")

horas = input("Digite a hora aqui: ")
minutos = input("Digite o minuto aqui: ")


if int(horas) >= 0 and int(horas) <= 11:
    print("Bom dia!")
if int(horas) >= 12 and int(horas) <= 17:
    print("Boa tarde!")
if int(horas) >= 18 and int(horas) <= 23:
    print("boa noite!")