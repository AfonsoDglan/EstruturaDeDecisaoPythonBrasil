# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
shift = str(input('Enter the shift on what your study: "M"-matutino, "V"-vespertino, "N"-noturno: '));
if shift.lower() == 'm':
    print('Bom Dia!');
elif shift.lower() == 'v':
    print('Boa Tarde!');
elif shift.lower() == 'n':
    print('Boa Noite!');
else:print('Valor Inválido!');

