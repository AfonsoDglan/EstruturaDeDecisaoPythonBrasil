n1 = float(input('Enter the first note: '));
n2 = float(input('Enter the second note: '));
media = (n1+n2)/2;
if media == 10:
    print(f'Aprovado com Distinção.');
elif media >= 7:
    print(f'Aprovado.');
elif media < 7:
    print(f'Reprovado.');
else:print('ERROR');