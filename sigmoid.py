import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-5, 5, 1000)
#sigmoid becomes steeper as c increases, behaving like a step function and percepton, except for when z = 0
for c in [1, 5, 20, 100]:
    plt.plot(z, 1 / (1 + np.exp(-c*z)), label=f'c={c}')
plt.legend()
plt.title("Sigmoid(cz) for increasing c")
plt.grid(True)
plt.show()

