''' 
Un taxi cobra $35 de banderazo y $9 por kilómetro recorrido. Los viajes de más de 20 km tienen 10% de 
descuento. Se necesita mostrar el importe del viaje.
''' 
#PROBLEMA
# Solicitar al usuario la cantidad de kilómetros recorridos y calcular el importe del viaje según las condiciones dadas.

# ENTRADAS
# costo_banderazo = 35
# costo_km = 9
# descuento = 0.10

#SALIDAS: (lo que se muestra, con su tipo y formato)
# Importe del viaje en pesos.
# importe_viaje: float

#REGLAS Y SUPUESTOS: (valores fijos, límites exactos (< o <=) y redondeo).
# - El costo del banderazo es de $35.
# - El costo por kilómetro es de $9.
# - El descuento del 10% se aplica a viajes de más de 20 km.


#ALGORITMO: pasos numerados con las fórmulas. 
# 1. leer costo_banderazo
# 2. leer costo_km
# 3. leer descuento
# 4. leer distancia
# 5. calcular importe_viaje = costo_banderazo + (costo_km * distancia)
# 6. si distancia > 20 entonces
# 7. aplicar descuento
# 8. mostrar importe_viaje

#CASOS DE PRUEBA: entradas y resultado esperado, calculado a mano.
# caso 1: distancia = 5, importe_viaje = 35 + (9 * 5) = 35 + 45 = 80
# caso 2: distancia = 20, importe_viaje = 35 + (9 * 20) = 35 + 180 = 215
# caso 3: distancia = 21, importe_viaje = 35 + (9 * 21) = 35 + 189 = 224 - 10% = 201.6
# caso 4: distancia = 30, importe_viaje = 35 + (9 * 30) = 35 + 270 = 305 - 10% = 274.5

#RESTRICCIONES PARA EL AGENTE: lo que Copilot no debe agregar. Indica que la única biblioteca permitida es tabulate.
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES: nombre, parámetros y valor de retorno de cada función.
# leer_distancia() -> float
# calcular_importe_viaje(distancia: float) -> float
# mostrar_importe_viaje(importe_viaje: float) -> None

def leer_distancia() -> float:
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
    return distancia

def calcular_importe_viaje(distancia: float) -> float:
    costo_banderazo = 35
    costo_km = 9
    descuento = 0.10

    importe_viaje = costo_banderazo + (costo_km * distancia)
    if distancia > 20:
        importe_viaje -= importe_viaje * descuento
    return importe_viaje

def mostrar_importe_viaje(importe_viaje: float) -> None:
    print(f"El importe del viaje es: ${importe_viaje:.2f}")
    