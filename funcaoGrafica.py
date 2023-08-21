import matplotlib.pyplot as plt
import numpy as np

def scale():
    dbase = float(input("Enter the base damage: "))
    StatScale = input("Enter the scaling type (E/D/C/B/A/S): ")
    scaling = 0
    str = 10
    dex = 10
    scale = 0.05
    scale2 = 0.05
    y = [dbase]
    x = [10]

    for i in range(1, 90):

        if str <= 10:
            scale += 0.035
        elif 10 < str <= 20:
            scale += 0.0255 
        elif 20 < str :
            scale += 0.0025

        if dex <= 10:
            scale2 += 0.035
        elif 10 < dex <= 20:
            scale2 += 0.0255 
        elif 20 < dex :
            scale2 += 0.0025

        if  StatScale == "E":
            scaling = 0.24
        elif StatScale == "D":
            scaling = 0.49
        elif StatScale == "C":
            scaling = 0.74
        elif StatScale == "B":
            scaling = 0.99
        elif StatScale == "A":
            scaling = 1.39
        elif StatScale == "S":
            scaling = 2.00

        y.append(dbase + dbase * scaling * scale)
        x.append(x[i-1] + 1)

    return x, y

x, y = scale()

plt.xticks(x)
plt.yticks(y)
plt.plot(x, y, color='red')
plt.xlabel('Level')
plt.ylabel('Damage')
plt.title('Escaling damage')
plt.legend(loc='upper left')
plt.show()