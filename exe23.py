# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
n = float(input('Digite um número: '));
n = str(n);
n = list(n);
indice = n.index('.');
verificacao = n[indice+1:]
tamanho = len(verificacao);
if tamanho == 1:
    if verificacao[0] == '0':
        print('O número digitado é inteiro.');
    else: print('O número digitado é decimal.');
else:
    print('O número digitado é decimal.');