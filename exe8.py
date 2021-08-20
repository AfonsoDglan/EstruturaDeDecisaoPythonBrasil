# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo
# que a decisão é sempre pelo mais barato.
n1 = float(input('Enter the price of spaghetti: '));
n2 = float(input('Enter the price of soda: '));
n3 = float(input('Enter the price of banana: '));
if n1 < n2 and n1 < n3:
    print('The best option is spaghetti.');
elif n2 < n1 and n2 < n3:
    print('The best option is soda.');
elif n3 < n1 and n3 < n2:
    print('The best option is banana.');
else:print('ERROR');