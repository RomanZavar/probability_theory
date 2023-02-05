import numpy as np
import scipy.stats as st



np.random.seed(0)
data = np.random.randint(10, 30, 256)


print(f'Размер выборки n={len(data)},\n'
      f'доверительный интервал = {st.norm.interval(alpha=0.95, loc=np.mean(80), scale=st.sem(data))}' )




