n1 = float(input('Enter the first note: '));
n2 = float(input('Enter the second note: '));
media = (n1+n2)/2;
print(f'A média: {media}');
if media > 9 and media <= 10:
    print('Nota: "A"');
    print('Aprovado');
elif media > 7.5 and media <= 9:
    print('Nota: "B"');
    print('Aprovado');
elif media > 6 and media <= 7.5:
    print('Nota: "C"');
    print('Aprovado');
elif media > 4 and media <= 6:
    print('Nota: "D"');
    print('Reprovado');
elif media >= 0 and media <= 4:
    print('Nota: "E"');
    print('Reprovado');