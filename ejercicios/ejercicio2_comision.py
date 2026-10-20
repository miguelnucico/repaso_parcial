''' 
Un vendedor gana 5% de comisión sobre sus ventas del mes. Si vende $10,000 o más, la comisión es de 
8%. Si vende más de $50,000, recibe además un bono de $1,000. Se necesita mostrar la comisión, el bono 
y el total a pagar. 
''' 
#PROBLEMA
# Solicitar al usuario el monto de ventas del mes y calcular la comisión, el bono y el total a pagar según las condiciones dadas.

# ENTRADAS
# comision_mes = 0.05
# comision_ventas_altas = 0.08
# bono_ventas_altas = 1000

#SALIDAS: (lo que se muestra, con su tipo y formato)
# comision: float
# bono: float
# total_a_pagar: float

#REGLAS Y SUPUESTOS: (valores fijos, límites exactos (< o <=) y redondeo).
# - La comisión es del 5% sobre las ventas del mes.
# - Si las ventas del mes son de $10,000 o más, la comisión es del 8%.
# - Si las ventas del mes son de más de $50,000, además de la comisión del 8%, se recibe un bono de $1,000.


#ALGORITMO: pasos numerados con las fórmulas. 
# 1. leer ventas_mes
# 2. calcular comision = ventas_mes * comision_mes
# 3. si ventas_mes >= 10000 entonces
# 4. comision = ventas_mes * comision_ventas_altas
# 5. si ventas_mes > 50000 entonces
# 6. bono = bono_ventas_altas
# 7. total_a_pagar = comision + bono
# 8. mostrar total_a_pagar

#CASOS DE PRUEBA: entradas y resultado esperado, calculado a mano.
# caso 1: ventas_mes = 5000, comision = 5000 * 0.05 = 250, total_a_pagar = 250
# caso 2: ventas_mes = 10000, comision = 10000 * 0.08 = 800, total_a_pagar = 800
# caso 3: ventas_mes = 50000, comision = 50000 * 0.08 = 4000, bono = 1000, total_a_pagar = 5000
# caso 4: ventas_mes = 50001, comision = 50001 * 0.08 = 4000.08, bono = 1000, total_a_pagar = 5000.08

#RESTRICCIONES PARA EL AGENTE: lo que Copilot no debe agregar. Indica que la única biblioteca permitida es tabulate.
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES: nombre, parámetros y valor de retorno de cada función.
# leer_ventas_mes() -> float
# calcular_comision(ventas_mes: float) -> float
# mostrar_total_a_pagar(total_a_pagar: float) -> None

def leer_ventas_mes() -> float:
    ventas_mes = float(input("Ingrese el monto de ventas del mes: "))
    return ventas_mes

def calcular_comision(ventas_mes: float) -> float:
    comision_mes = 0.05
    comision_ventas_altas = 0.08
    bono_ventas_altas = 1000

    if ventas_mes >= 10000:
        comision = ventas_mes * comision_ventas_altas
    else:
        comision = ventas_mes * comision_mes

    if ventas_mes > 50000:
        bono = bono_ventas_altas
    else:
        bono = 0

    total_a_pagar = comision + bono
    return total_a_pagar

def mostrar_total_a_pagar(total_a_pagar: float) -> None:
    print(f"El total a pagar es: ${total_a_pagar:.2f}")