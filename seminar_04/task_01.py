#Случайная непрерывная величина A имеет равномерное распределение на
#промежутке (200, 800].
#Найдите ее среднее значение и дисперсию.

def mean_and_variance(a,b):
    return f'На промежутке ({a};{b}]\nСреднее значение: М(А) = {(a+b)/2: .2f}\n, Дисперсия: D(A) = {((b-a)**2)/12: .2f}'
print(mean_and_variance(200,800))