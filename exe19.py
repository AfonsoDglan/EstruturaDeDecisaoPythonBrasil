n = int(input('Digite um número inteiro menor que 1000: '));
if n < 1000:
    n = str(n)
    n=list(n);
    tamanho = len(n);
    if tamanho == 3:
        print(f'{"".join(n)} = {n[0]} centenas, {n[1]} dezenas e {n[2]} unidades.');
    elif tamanho == 2:
        print(f'{"".join(n)} = {n[0]} dezenas e {n[1]} unidades.');
    elif tamanho == 1:
        print(f'{"".join(n)} = {n[0]} unidades. ')