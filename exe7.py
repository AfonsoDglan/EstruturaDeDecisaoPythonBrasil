n1 = float(input('Enter the first number: '));
n2 = float(input('Enter the second number: '));
n3 = float(input('Enter the thrid number: '));
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'The first number is the bigger is the third is the smaller.');
elif n2 > n3 and n2 > n1 and n1 > n3:
    print('The second number is the bigger is the third is the smaller.');
elif n3 > n1 and n3 > n2 and n2 > n1:
    print('The third number is the bigger is the first is the smaller.');
elif n1 > n2 and n1 > n3 and n3 >  n2:
    print(f'The first number is the bigger is the second is the smaller.');
elif n2 > n3 and n2 > n1 and n3 > n1:
    print('The second number is the bigger is the first is the smaller.');
elif n3 > n1 and n3 > n2 and n1 > n2:
    print('The third number is the bigger is the second is the smaller.');