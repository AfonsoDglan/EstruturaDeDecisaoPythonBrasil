data = str(input('Digite a data no formato dd/mm/aaaa:')).split('/');
if int(data[0]) >= 1 and int(data[0]) <= 31 and int(data[1]) >= 1 and int(data[1]) <= 12 and int(data[2]) > 0:
    print('Data válida!');
else:print('Data Inválida!');