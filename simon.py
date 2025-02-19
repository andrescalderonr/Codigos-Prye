import matplotlib.pyplot as plt
import statistics as stats
import seaborn as sns
import numpy as np
def grafica():
    # Datos que se van a graficar
    sin_envejecimiento = [227, 222, 218, 217, 225, 218, 216, 129, 228, 221]
    con_envejecimiento = [219, 214, 215, 211, 209, 218, 203, 204, 201, 205]
    indice = [1,2,3,4,5,6,7,8,9,10]

    # Gráfica
    plt.scatter(indice, sin_envejecimiento, color='blue', label='Sin envejecimiento', alpha=0.7)
    plt.scatter(indice, con_envejecimiento, color='red', label='Con envejecimiento', alpha=0.7)

    # Etiquetas y título
    plt.title('Resistencia a la tension', fontsize=14)
    plt.xlabel('Indice', fontsize=12)
    plt.ylabel('Valores (psi)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # Mostrar
    plt.show()

def media():
    sin_envejecimiento = [106,116,125,134,138,142,146,153,163,165,175,179]

    media1 = round(stats.mean(sin_envejecimiento),3)


    print("Media de polimero sin envejecimiento:",+ media1)

def mediana():
    sin_envejecimiento = [227, 222, 218, 217, 225, 218, 216, 129, 228, 221]
    con_envejecimiento = [219, 214, 215, 211, 209, 218, 203, 204, 201, 205]

    mediana1 = stats.median(sin_envejecimiento)
    mediana2 = stats.median(con_envejecimiento)

    print("Mediana de polimero sin envejecimiento:",+ mediana1)
    print("Mediana de polimero con envejecimiento:",+ mediana2)

def varianza_desviacion():
    sin_envejecimiento = [100,103,108,118,125,127,136,140,143,148,156,166,168,171,176,181]
    
    varianza1 = round(stats.variance(sin_envejecimiento),3)
    desviacion1 = stats.stdev(sin_envejecimiento)

  

    print("Varianza sin envejecimiento es de:",+varianza1)
    print("Desviacion estandar sin envejecimeinto es de:", + desviacion1)


def grafica_caja():
    altura = [1.54,1.55,1.58,1.75,1.75,1.87,1.73,1.84,1.79,1.78,1.83,1.70,1.65,1.69,1.59,1.68,1.64,1.69,1.57,1.74,1.75,1.75,1.65,1.54,1.61,1.74,1.56]
    altura.sort()
    sns.boxplot(altura)
    plt.ylabel("Altura",fontsize = 12)
    plt.show()

def edad():
    edad = [18,20,20,19,20,21,18,21,18,19,20,20,21,22,23,19,19,19,19,19,22,20,21,19,19,22,20]
    edad.sort()
    sns.boxplot(y = edad)
    plt.ylabel("Edad",fontsize = 12)
    plt.show()

def tiempo():
    tiempo = [20  ,45 ,10 ,90 ,70 ,90 ,30 ,30 ,20 ,90 ,50 ,90 ,35 ,30 ,90 ,40 ,20 ,40 ,90 ,30 ,25,35 ,90 ,39 ,110 ,40 ,90]
    tiempo.sort()
    sns.boxplot( y = tiempo)
    plt.ylabel("Tiempo de trayecto a la U (min)",fontsize = 12)
    plt.show()

def alturac():
    altura = [1.54,1.55,1.58,1.75,1.75,1.87,1.73,1.84,1.79,1.78,1.83,1.70,1.65,1.69,1.59,1.68,1.64,1.69,1.57,1.74,1.75,1.75,1.65,1.54,1.61,1.74,1.56]
    altura.sort()
    sns.histplot(altura,stat="proportion")
    plt.xlabel("Altura",fontsize = 12)
    plt.show()

def trayecto():
    tiempo = [20  ,45 ,10 ,90 ,70 ,90 ,30 ,30 ,20 ,90 ,50 ,90 ,35 ,30 ,90 ,40 ,20 ,40 ,90 ,30 ,25,35 ,90 ,39 ,110 ,40 ,90]
    tiempo.sort()
    sns.histplot(tiempo, stat="proportion")
    plt.xlabel("Tiempo de trayecto a la U (min)",fontsize = 12)
    plt.show()

def asimetria_curtosis():
        # Datos
    X = np.array([106,116,125,134,138,142,146,153,163,165,175,179])

    # Parámetros conocidos
    x_mean = 141.625  # Media muestral
    s2 = 704.783      # Varianza muestral
    s = np.sqrt(s2)   # Desviación estándar
    n = len(X)        # Número de observaciones

    # Cálculo de asimetría (Sk)
    sk = np.sum((X - x_mean)**3) / (n * s**3)

    # Cálculo de curtosis (K)
    k = np.sum((X - x_mean)**4) / (n * s**4)

    # Redondeamos a 3 decimales
    sk = round(sk, 3)
    k = round(k, 3)

    print(f"Coeficiente de asimetría (Sk): {sk}")
    print(f"Coeficiente de curtosis (K): {k}")
asimetria_curtosis()