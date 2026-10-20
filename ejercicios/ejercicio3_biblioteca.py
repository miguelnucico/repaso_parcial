''' 
Una biblioteca cobra $5 por cada día de retraso en la devolución de un libro. A partir del día 11 de 
retraso, cada día cuesta $10. La multa máxima es de $200. Se necesita mostrar la multa a partir de los 
días de retraso.
''' 
#PROBLEMA
# Solicitar al usuario la cantidad de días de retraso y calcular la multa según las condiciones dadas.

# ENTRADAS
# costo_dia_retraso = 5
# costo_dia_retraso_alto = 10
# multa_maxima = 200

#SALIDAS: (lo que se muestra, con su tipo y formato)
# multa: float


#REGLAS Y SUPUESTOS: (valores fijos, límites exactos (< o <=) y redondeo).
# - El costo del día de retraso es de $5.
# - El costo por día de retraso a partir del día 11 es de $10.
# - La multa máxima es de $200.


#ALGORITMO: pasos numerados con las fórmulas. 
# 1. leer dias_retraso
# 2. calcular multa = dias_retraso * costo_dia_retraso
# 3. si dias_retraso > 10 entonces
# 4. multa = (10 * costo_dia_retraso) + ((dias_retraso - 10) * costo_dia_retraso_alto)
# 5. si multa > multa_maxima entonces
# 6. multa = multa_maxima
# 7. mostrar multa

#CASOS DE PRUEBA: entradas y resultado esperado, calculado a mano.
# caso 1: dias_retraso = 0, multa = 5 * 5 = 25
# caso 2: dias_retraso = 10, multa = 10 * 5 = 50
# caso 3: dias_retraso = 11, multa = (10 * 5) + (1 * 10) = 50 + 10 = 60
# caso 4: dias_retraso = 25, multa = (10 * 5) + (15 * 10) = 50 + 150 = 200
# caso 5: dias_retraso = 40, multa = (10 * 5) + (30 * 10) = 50 + 300 = 350 - 200 = 200

#RESTRICCIONES PARA EL AGENTE: lo que Copilot no debe agregar. Indica que la única biblioteca permitida es tabulate.
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES: nombre, parámetros y valor de retorno de cada función.
# leer_dias_retraso() -> float
# calcular_multa(dias_retraso: float) -> float
# mostrar_multa(multa: float) -> None

def leer_dias_retraso() -> float:
    dias_retraso = float(input("Ingrese la cantidad de días de retraso: "))
    return dias_retraso

def calcular_multa(dias_retraso: float) -> float:
    costo_dia_retraso = 5
    costo_dia_retraso_alto = 10
    multa_maxima = 200

    if dias_retraso <= 10:
        multa = dias_retraso * costo_dia_retraso
    else:
        multa = (10 * costo_dia_retraso) + ((dias_retraso - 10) * costo_dia_retraso_alto)

    if multa > multa_maxima:
        multa = multa_maxima

    return multa

def mostrar_multa(multa: float) -> None:
    print(f"La multa por retraso es: ${multa:.2f}")