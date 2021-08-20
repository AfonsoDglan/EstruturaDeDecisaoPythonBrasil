saque_valor= int(input('Digite o valor do saque: '));
notas=[1,5,10,50,100];
if saque_valor >= 10 and saque_valor <= 600:
    valor_str=str(saque_valor)
    valor_str=list(valor_str);
    tamanho = len(valor_str);
    valor_str[0] = int(valor_str[0]);
    valor_str[1] = int(valor_str[1]);
    if tamanho == 3:
        valor_str[2] = int(valor_str[2]);
        de_100=valor_str[0]
        print(f'O valor do Saque é de: {saque_valor}:');
        print(f'Notas de 100: {de_100}');
        if valor_str[1] >= 5:
            de_50 = 1;
            print(f'Notas de 50: {de_50}');
            valor_str[1] = valor_str[1] - 5;
            if valor_str[1] > 0:
                de_10 = valor_str[1];
                print(f'Notas de 10: {de_10}');
        else:
            de_10 = valor_str[1];
            print(f'Notas de 10: {de_10}');
        if valor_str[2] >= 5:
            de_5 = 1;
            print(f'Notas de 5: {de_5}');
            valor_str[2] = valor_str[2] - 5;
            if valor_str[2] > 0:
                de_1 = valor_str[2];
                print(f'Notas de 1: {de_1}');
        else:
            de_1 = valor_str[2];
            print(f'Notas de 1: {de_1}');
    else:
        if valor_str[0] >= 5:
            de_50 = 1;
            print(f'Notas de 50: {de_50}');
            valor_str[0] = valor_str[0] - 5;
            if valor_str[0] > 0:
                de_10 = valor_str[0];
                print(f'Notas de 10: {de_10}');
        else:
            de_10 = valor_str[1];
            print(f'Notas de 10: {de_10}');
        if valor_str[1] >= 5:
            de_5 = 1;
            print(f'Notas de 5: {de_5}');
            valor_str[1] = valor_str[1] - 5;
            if valor_str[1] > 0:
                de_1 = valor_str[1];
                print(f'Notas de 1: {de_1}');
        else:
            de_1 = valor_str[1];
            print(f'Notas de 1: {de_1}');