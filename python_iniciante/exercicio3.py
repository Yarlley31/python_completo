print("-" * 29)
print("Analisador de nomes")
print("-" * 29)

nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print(f"Seu nome é curto, ele tem {len(nome)} letras.")
if len(nome) >= 5 and len(nome) <= 6:
    print(f"Seu nome é normal, ele tem {len(nome)} letras.")
else:
    print(f"Seu nome é grande, ele tem {len(nome)} letras.")