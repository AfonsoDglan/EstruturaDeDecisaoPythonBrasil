# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
a = float(input('Digite o valor de "A": '));
if a != 0:
    b = float(input('Digite o valor de "B": '));
    c = float(input('digite o valor de "C": '));
    delta = (b**2)-4*a*c;
    if delta < 0:
        print('A equação não possui raizes reais.');
    elif delta == 0:
        print('A equação só possui uma raiz real.');
        raiz = (-b)/(2*a);
    elif delta > 0:
        raiz_delta = delta ** 0.5;
        raiz1 = ((-b) + raiz_delta)/2*a
        raiz2 = ((-b) - raiz_delta)/2*a
        print(f'As raizes reais da equação são {raiz1} e {raiz2}');
