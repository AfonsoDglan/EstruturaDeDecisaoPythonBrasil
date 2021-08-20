print('Para as perguntas responda "s" para sim e "n" para não.');
p1 = input("Telefonou para a vítima?").lower();
p2 = input("Esteve no local do crime?").lower();
p3 = input("Mora perto da vítima?").lower();
p4 = input("Devia para a vítima?").lower();
p5 = input("Já trabalhou com a vítima?").lower();
lista = [p1,p2,p3,p4,p5];
positivamente = lista.count('s');
if positivamente == 2:
    print('Você é uma pessoa Suspeita no caso.');
elif positivamente == 3 or positivamente == 4:
    print('Você é uma pessoa Cúmplice.');
elif positivamente == 5:
    print('Você é o Assassino.');
else:
    print('Você é uma pessoa Inocente.');