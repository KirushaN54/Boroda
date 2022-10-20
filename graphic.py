import numpy as np
import matplotlib.pyplot as plt

with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype=int)
data_array = 3.3*data_array/256

fig, ax = plt.subplots(figsize=(16,10), dpi=200)

x=np.arange(1,217,1)
x=x*tmp[0]
ax.plot(x, data_array, label = r'V=V(t)', color = "red")
ax.plot(x, data_array, 'ro', color = "blue", markersize = 1)

#дополнительные отметки на осях
plt.minorticks_on()

#подписи осей
plt.xlabel("Время, с" , fontsize=16)
plt.ylabel(r"Напряжение, В" , fontsize=16)

#заголовок
plt.title(r'Зависимость напряжения на конденсаторе от времени', fontsize=18)

#легенда
ax.legend(loc="best", fontsize = 12)

#major setka
plt.grid(which='major')

#additional setka
plt.grid(which='minor', linestyle=':')

#диапазон осей
plt.xlim([0, 90])  
plt.ylim([0, 3.5])

#время зарядки и разрядки
plt.text(70, 2.5, r'Время зарядки = 45с')
plt.text(70, 2.25, r'Время разрядки = 42с')

fig.savefig("graphic.svg")
plt.show()          
