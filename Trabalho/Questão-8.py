n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print()
print('Operações:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Divisão')
print('4 - Multiplicação')
print()
ope = int(input('Escolha o número da operação desejada: '))
if ope == 1:
    resultado = n1 + n2
elif ope == 2:
    resultado = n1 - n2
elif ope == 3:
    resultado = n1 / n2
elif ope == 4:
    resultado = n1 * n2            
print()
print('O resultado é', resultado ,'!')
print()