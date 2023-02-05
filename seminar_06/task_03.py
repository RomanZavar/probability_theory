import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


ks = np.array([75, 167, 154, 174, 178, 148, 160, 167, 169, 170])
ms = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])



def mean(dataset):
    return sum(dataset) / len(dataset)

print(f'Cредний рост детей = {mean(ks)}\n'
      f'Средний рост родителей = {mean(ms)}')


data = ([mean(ks), mean(ms)])
print(f'доверительный интервал среднего = {st.norm.interval(alpha=0.95, loc=np.mean(data), scale=st.sem(data))}' )
