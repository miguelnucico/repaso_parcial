from ejercicios.ejercicio1_sueldo import leer_horas_trabajadas, calcular_sueldo, mostrar_sueldo
from ejercicios.ejercicio2_comision import leer_ventas_mes, calcular_comision, mostrar_total_a_pagar
from ejercicios.ejercicio3_biblioteca import leer_dias_retraso, calcular_multa, mostrar_multa

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Calcular sueldo")
        print("2. Calcular comisión")
        print("3. Calcular multa por retraso de libro")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            horas_trabajadas = leer_horas_trabajadas()
            sueldo = calcular_sueldo(horas_trabajadas)
            mostrar_sueldo(sueldo)
        elif opcion == "2":
            ventas_mes = leer_ventas_mes()
            total_a_pagar = calcular_comision(ventas_mes)
            mostrar_total_a_pagar(total_a_pagar)
        elif opcion == "3":
            dias_retraso = leer_dias_retraso()
            multa = calcular_multa(dias_retraso)
            mostrar_multa(multa)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")