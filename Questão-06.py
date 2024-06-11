nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
print()
if idade < 16:
    print(f'{nome}, você ainda não tem idade para tirar o título de eleitor!')
else:
    print(f'{nome}, você já pode tirar seu título de eleitor!')
