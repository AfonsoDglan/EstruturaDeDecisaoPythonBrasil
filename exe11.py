salary = float(input('Enter the your salary: '));
percentual = 0;
if salary <= 280:
    aumento = (salary*20/100);
    percentual = 20;
elif salary > 280 and salary <= 700:
    aumento = (salary*15/100);
    percentual = 15;
elif salary > 700 and salary <=1500:
    aumento = (salary*10/100);
    percentual = 10;
elif salary > 1500:
    aumento = (salary*5/100);
    percentual = 5;
print(f'O salário antes do reajuste: {salary}');
print(f'O percentual de aumento aplicado: {percentual}');
print(f'O valor do aumento: {aumento}');
print(f'O novo salário, após o aumento: {salary+aumento}')