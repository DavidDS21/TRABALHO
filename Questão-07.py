print()
nome = input('Digite o nome do aluno: ')
dic = input('Digite a diciplina: ')
print()
n1 = float(input('Digite sua nota parcial: '))
n2 = float(input('Digite sua nota bimestral: '))
med = float((n1+n2)/2)
print('Média:', med)
print()
situação1 = 'Aprovado'
situação2 = 'Reprovado'
if med >= 6 and med <= 10:
    print(f'{nome} está {situação1} na diciplina {dic}')
else:
    print(f'{nome} está {situação2} na diciplina {dic}')
print()
