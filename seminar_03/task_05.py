


P3=0.1*0.2*0.25
print(f'Вероятность того, что из строя выйдут все детали Р(3) = {P3: .3f}')

P2=0.1*0.2*0.75+0.1*0.25*0.8+0.2*0.25*0.9
print(f'Вероятность того, что из строя выйдут только 2 детали Р(2) = {P2: .2f}')

P0=0.9*0.8*0.75
print(f'Вероятность того, что из строя не выйдет ни 1 деталь Р(0) = {P0: .4f}')

P_0=1-P0
print(f'Вероятность того, что выйдет из строя хотя бы одна деталь Р(>=1) = {P_0:.2f}')

P1=0.1*0.8*0.75+0.2*0.9*0.75+0.25*0.9*0.8
print(f'Вероятность того, что выйдет из строя одна деталь Р(1) = {P1: .2f}')

print(f'вероятность что выйдут из строя от одной до двух {P1+P2}')