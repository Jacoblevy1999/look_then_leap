import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from look_then_leap import SecretaryProblem, Simulation


s = Simulation(1000, 100, 1000000)
y_vals = s.simulate()
x_vals = []
x_ticks = []
x_val_distances = []
for i in range(0, 100):
    x_vals.append(i)
    if i % 10 == 0:
        x_ticks.append(i)
    x_val_distances.append(100)

plt.bar(x_vals, y_vals, align='center', alpha=0.5)
plt.xticks(x_ticks)
plt.ylabel('% Correct')
plt.xlabel('When the Employer Changed from Looking to Leaping')
plt.title('Simulation of Secretary problem')

plt.show()