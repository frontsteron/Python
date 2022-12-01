# Постройте график функции 𝑓 𝑥 = 5𝑥^2 + 10𝑥 − 30
# По графику определите, при каких значения x значение функции отрицательно.

import numpy as np
import matplotlib.pyplot as plt
 
y = lambda x: (5*x*x)+(10*x)-30

xs = np.linspace(-10, 10, 20)

plt.plot(xs, [y(x) for x in xs])
plt.show()