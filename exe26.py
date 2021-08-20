print('TIPO DE COMBUSTÍVEL');
tipo = input('A-álcool\nG-gasolina\nOpção: ').lower();
litros = float(input('Digite quantos litros deseja: '));
if tipo == 'a':
    total = litros * 1.90;
    if litros <= 20:
        total -= (total*3/100);
    elif litros > 20:
        total -= (total*5/100);
elif tipo == 'g':
    total = litros * 2.50;
    if litros <= 20:
        total -= (total*4/100);
    elif litros > 20:
        total -= (total*6/100);
print(f'O valor a ser pago é: {total}');
