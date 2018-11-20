
import math

print("Ingresar coordenada ")

x=float(input("Ingrese  coordenada en X"))

y=float(input("Ingrese coordenada en Y"))

distancia=(x-y)
if distancia<0:
    distancia=distancia*(-1)

dis0=math.sqrt(x**2+y**2)
print()
print("la distancia entre ambos puntos es:  ",distancia)
print("la distancia de la coordenada al punto 0,0 es:",dis0)
