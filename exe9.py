# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input('Enter the first number: '));
n2 = float(input('Enter the second number: '));
n3 = float(input('Enter the third number: '));
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'{n1}, {n2}, {n3}');
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'{n1}, {n3}, {n2}');
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f'{n2}, {n1}, {n3}');
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f'{n2}, {n3}, {n1}');
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'{n3}, {n1}, {n2}');
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(f'{n3}, {n2}, {n1}');
else:print('ERROR');