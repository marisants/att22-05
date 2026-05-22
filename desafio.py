print("************************")
print("TAXA METABÓLICA BASAL")
print("************************")
a = float(input('digite seu peso em kg: '))
b = float(input('digite sua altura em metros: '))
c = float(input('digite sua idade: '))

resultado = (10*a) + (6.25*b) - (5*c) + 5

print(f'sua BMR é {resultado:.1f}')