valor_horas = float(input('Digite o valor da sua hora de trabalho: '));
horas_trabalhadas = float(input('Digite o total de horas trabalhadas neste mês: '));
salario_bruto = valor_horas*horas_trabalhadas;
print(f'Salário Bruto: ({valor_horas} * {horas_trabalhadas})        : R$ {salario_bruto}');
ir = 0;
if salario_bruto <= 900:
    print(f'(-) IR (isento) ');
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = (salario_bruto*5/100);
    print(f'(-) IR (5%)                     : R$ {ir} ');
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = (salario_bruto*10/100)
    print(f'(-) IR (10%)                     : R$ {ir} ');
elif salario_bruto > 2500:
    ir = (salario_bruto*20/100);
    print(f'(-) IR (10%)                     : R$  {ir} ');
sindicato = (salario_bruto*3/100)
print(f'(-) Sindicato (3%)           : {sindicato}');
inss = (salario_bruto*10/100);
print(f'(-) INSS ( 10%)                 : R$ {inss}');
fgts = (salario_bruto*11/100)
print(f'FGTS (11%)                      : R$ {fgts} ');
Total_descontos = ir + sindicato + inss;
print(f'Total de descontos              : R$  {Total_descontos}');
print(f'Salário Liquido                 : R$  {salario_bruto-Total_descontos}');