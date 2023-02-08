#Даны значения зарплат из выборки выпускников: 
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 
# 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических
# -методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np


arr=np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

def mean_value(array):
    return sum(array)/len(array)



def mean_square_deviation(array):
    square_dev=(array-mean_value(array))**2
    return (sum(square_dev)/len(square_dev))**(1/2)



def dispers(array, no_off=False):

    square_dev=(array-mean_value(array))**2
    return sum(square_dev)/(len(square_dev)-1) if no_off else sum(square_dev)/len(square_dev)

print(f'Среднее арифметическое выборки М(Х) = {mean_value(arr): .2f} '
      f'Среднее квадратичное отклонение для данной выборки CKO = {mean_square_deviation(arr): .4f} '
      f'Смещенная оценка дисперсии для данной выборки D = {dispers(arr): .4f}\n'
      f'Немещенная оценка дисперсии для данной выборки D = {dispers(arr, True): .4f}\n'
     )  


def test_function(arr):
    np.mean(arr)
    np.std(arr)
    np.var(arr)
print(f'М(Х)={np.mean(arr)}\n'
      f'CKO={np.std(arr)}\n'
      f'SD={np.std(arr)}\n'
      f'D={ np.var(arr)}' )