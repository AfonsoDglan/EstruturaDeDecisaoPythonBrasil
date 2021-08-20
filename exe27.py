morango_kg = float(input('quantidade (em Kg) de morangos: '));
maca_kg = float(input('quantidade (em Kg) de maças: '));
if morango_kg <= 5:
    valor_morango = morango_kg * 2.50;
elif morango_kg > 5:
    valor_morango = morango_kg * 2.20;
if maca_kg <= 5:
    valor_maca = maca_kg * 1.80;
elif maca_kg > 5:
    valor_maca = maca_kg * 1.50;
valor_total = valor_maca + valor_morango;
kg_total = morango_kg+maca_kg;
if valor_total > 25 or kg_total > 8:
    valor_total -= (valor_total*10/100);
    print(f'Valor total: {valor_total}')
else:print(f'Valor total: {valor_total}');
