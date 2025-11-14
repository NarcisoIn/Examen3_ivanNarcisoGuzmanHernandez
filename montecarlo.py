# Hecho por Iván Narciso
# Cálculo por el metodo de montecarlo
import random
import math


def metodo_montecarlo_pi(num_puntos):
    puntos_dentro = 0

    # Generar puntos aleatorios
    for _ in range(num_puntos):
        x = random.random()  # número aleatorio entre 0 y 1
        y = random.random()  # número aleatorio entre 0 y 1

        # Verificar si el punto (x, y) cae dentro del círculo
        if x**2 + y**2 <= 1:
            puntos_dentro += 1

    # Calcular aproximación de pi
    pi_aproximado = 4 * puntos_dentro / num_puntos
    return pi_aproximado


# Ejemplo de uso
num_puntos = 10000000  # mientras más puntos, más precisión
pi_estimado = metodo_montecarlo_pi(num_puntos)

print(f"Aproximación de π con {num_puntos} puntos: {pi_estimado}")
print(f"Error respecto a math.pi: {abs(math.pi - pi_estimado)}")
