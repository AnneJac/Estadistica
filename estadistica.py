import matplotlib.pyplot as plt # importando matplotlib
import seaborn as sns # importando seaborn
import pandas as pd
import numpy as np
import matplotlib


ListaEmpleados = pd.read_csv ('empleados.csv')
select = ListaEmpleados [['TotalAtaque']]


media = select.mean()[0] #media
desvStd = np.std (select) #disviacion estandar
mediana = np.median (select) #mediana
varianza = np.var (select)[0] #varianza

print("Media = " +str(media))
print("Desviación std =" +str (desvStd))
print("Mediana = " +str(mediana))
print ("Varianza = " +str (varianza))

sd = select.as_matrix

# histogrma de distribución normal
cuenta, cajas , ignorar = plt.hist(sd, 20)

#Trazo de la media y la desviación estandar
plt.axvline(media , color = 'b')
plt.axvline(media -desvStd, color = 'r')
plt.axvline(media +desvStd, color = 'r')

# Mostrar la grafica
plt.show()