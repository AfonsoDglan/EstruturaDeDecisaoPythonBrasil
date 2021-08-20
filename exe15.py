l1 = float(input('Enter the first side: '));
l2 = float(input('Enter the second side: '));
l3 = float(input('Enter the third side: '));
if l1+l2 > l3 or l1+l3 > l2 or l2+l3 > l1:
    if l1 == l2 == l3:
        print('Triângulo Equilátero.');
    elif l1 != l2 != l3:
        print('Triângulo Escaleno');
    else:
        print('Triângulo Isósceles');
else:print('Não pode ser um triângulo.');