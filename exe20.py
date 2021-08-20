n1 = float(input('Enter the first note: '));
n2 = float(input('Enter the second note: '));
n3 = float(input('Enter the third note: '));
media = (n1+n2+n3)/3
if media >= 7 and media < 10:
    print('Aprovado.');
elif media < 7:
    print('Reprovado.');
elif media == 10:
    print('Aprovado com Distinção.');
else:print('ERROR.')