
# inteiro ou decimal
n1 = float(input('Digite um número: '));
n2 = float(input('Digite outro número: '));
operacao = int(input('1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\nDigite a opção:'));
if operacao == 1:
    resultado = n1+n2;
elif operacao == 2:
    resultado = n1-n2;
elif operacao == 3:
    resultado = n1*n2;
elif operacao == 4:
    resultado = n1/n2;
else:print('Opção não encontrada.')
print(f'O resultado da operação: {resultado}');
if resultado%2 == 0:
    print('O resultado é par.');
else:print('O resultado é ímpar.');
if resultado >= 0:
    print('O resultado é positivo.');
else:print('O resultado é negativo.');
resultado = str(resultado);
resultado = list(resultado);
indice = resultado.index('.');
verificacao = resultado[indice+1:]
tamanho = len(verificacao);
if tamanho == 1:
    if verificacao[0] == '0':
        print('O resultado é inteiro.');
    else: print('O resultado é decimal.');
else:
    print('O resultado é decimal.');
