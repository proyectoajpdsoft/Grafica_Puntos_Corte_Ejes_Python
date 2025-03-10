import matplotlib.pyplot as plt
import numpy as np

# Función FX definida (en este caso, la F(x) = x^2 - 4)
def f(x):
    return x**2 - 4

# Creamos un rango de valores para x
x = np.linspace(-5, 5, 100)
# Asignamos a y la función f(x)
y = f(x)

# Creamos la figura y el eje
fig, ax = plt.subplots()

# Graficamos la función
ax.plot(x, y)

# Configurar los ejes para que solo se muestren los ejes X e Y y no los bordes
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Mostrar los valores en los ejes
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Añadir etiquetas a los ejes
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Agregamos la leyenda al gráfico, fuera del gráfico, arriba a la derecha
# Usamos notación especial para mostrar correctamente los exponentes
plt.legend([r"f(x) = $x^{2} - 4$"], bbox_to_anchor = (1.1, 1), loc = "lower right",  prop={"size": 6})

# Establecemos el color y grosor de la línea divisora del eje X
plt.axhline(0, color = "black", lw = 1, linestyle = "--")
# Establecemos el color y grosor de la línea divisora del eje Y
plt.axvline(0, color = "black", lw = 1, linestyle = "--")

# Para mostrar los puntos de corte con los ejes, deberemos conocer la solución de la ecuación
# que nos dará los tres puntos de corte: (-2, 0), (2, 0) y (0,-4)
plt.scatter(-2, 0, color = "red", zorder = 5)
plt.scatter(2, 0, color = "red", zorder = 5)
plt.scatter(0, -4, color = "red", zorder = 5)
plt.text(-2, 0, "(-2, 0)", fontsize = 8, verticalalignment = "bottom")
plt.text(2, 0, "(2, 0)", fontsize = 8, verticalalignment = "bottom")
plt.text(0, -4, "(0,-4)", fontsize = 8, verticalalignment = "bottom")

# Título del gráfico, donde usamos notación para mostrar el exponente de forma correcta gráficamente
plt.title(r"Gráfica de la función f(x) = $x^{2} - 4$")
plt.xlabel("X")
plt.ylabel("Y")

# Mostramos el gráfico con una rejilla
plt.grid(True)
plt.show()