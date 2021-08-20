ano = int(input('Digite o ano que quer conferir se é bisesto: '));
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('Ano Bisesto.');
else:
    print('Ano não Bisesto.');