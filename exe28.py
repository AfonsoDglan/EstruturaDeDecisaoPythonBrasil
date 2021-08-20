# e valor a pagar.
tipo_carne = int(input('1-File Duplo\n2-Alcatra\n3-Picanha\nOpção: '));
carne_kg = float(input('Quantidade (em Kg) de carne: '));
pagamento = str(input('Deseja fazer o pagamento com o cartão Tabajara "S" para sim e "n" para não: ')).lower();
tipo = '';
if tipo_carne == 1:
    if carne_kg <= 5:
        preco_total = carne_kg * 4.90;
    elif carne_kg > 5:
        preco_total = carne_kg * 5.80;
    tipo = 'File Duplo';
elif tipo_carne == 2:
    if carne_kg <= 5:
        preco_total = carne_kg * 5.90;
    elif carne_kg > 5:
        preco_total = carne_kg * 6.80;
    tipo = 'Alcatra';
elif tipo_carne == 3:
    if carne_kg <= 5:
        preco_total = carne_kg * 6.90;
    elif carne_kg > 5:
        preco_total = carne_kg * 7.80;
    tipo = 'Picanha';
print('*'*20,' Cupom Físcal ','*'*20);
print(f'Tipo de carne: {tipo}');
print(f'Quantidade de carne: {carne_kg}Kg');
print(f'Preço Total: R${preco_total}');
if pagamento == 's':
    cartao =  (preco_total*5/100);
    print(f'Tipo de pagamento: No cartão Tabajara');
    print(f'Valor do desconto: R${cartao}');
    print(f'Valor a ser pago: {preco_total-cartao}');
elif pagamento == 'n':
    print(f'Tipo de pagamento: Dinheiro em especie.');
    print('Valor do desconto: R$ 00');
    print(f'Valor a ser pago: {preco_total}');
