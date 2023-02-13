#Рост взрослого населения города X 
# имеет нормальное распределение, причем, средний рост равен 174 см,
#  а среднее квадратическое отклонение равно 8 см. посчитайте, 
# какова вероятность того, что случайным образом выбранный взрослый
#  человек имеет рост:
#1. больше 182 см?
#2. больше 190 см?
#3. от 166 см до 190 см?
#4. от 166 см до 182 см?
#5. от 158 см до 190 см?
#6. не выше 150 см или не ниже 190 см?
#7. не выше 150 см или не ниже 198 см?
#8. ниже 166 см?

from statistics import NormalDist

def z_value(height):
    return (height-174)/8

z_value(182)
P1=1-NormalDist().cdf(z_value(182))


z=z_value(190)
P2=1-NormalDist().cdf(z)

z1=z_value(166)
z2=z_value(190)
P3=NormalDist().cdf(z2)-NormalDist().cdf(z1)

z1=z_value(166)
z2=z_value(182)
P4=NormalDist().cdf(z2)-NormalDist().cdf(z1)

z1=z_value(158)
z2=z_value(190)
P5=NormalDist().cdf(z2)-NormalDist().cdf(z1)


z1=z_value(150)
z2=z_value(190)
P6=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))


z1=z_value(150)
z2=z_value(198)
P7=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))


z=z_value(166)
P8=NormalDist().cdf(z)


print(f'больше 182 ={P1: .4f};\n'
      f'больше 190 ={P2: .4f};\n'
      f'от 166 см до 190 см ={P3: .4f};\n'
      f'от 166 см до 182 см ={P4: .4f};\n'
      f'от 158 см до 190 см ={P5: .4f};\n'
      f'не выше 150 см или не ниже 190 см = {P6: .4f};\n'
      f'не выше 150 см или не ниже 198 см = {P7: .4f};\n'
      f'ниже 166 см ={P8: .4f};\n')