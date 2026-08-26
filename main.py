# =============================================================================
# BANCO DE ALIMENTOS - MEDELLÍN
# Archivo: main.py
# Contiene la función principal que orquesta el flujo del programa
# =============================================================================

from funciones import (
    registrar_hogares,
    validar_hogar,
    calcular_puntaje,
    clasificar_prioridad,
    registrar_entregas,
    generar_resumen
)


def main():
    """
    Función principal que ejecuta el flujo completo del programa.
    """
    print("=" * 50)
    print("BANCO DE ALIMENTOS - MEDELLÍN")
    print("Sistema de registro y control de entregas")
    print("=" * 50)
    
    # Paso 1: Registrar 12 hogares
    print("\n>> FASE 1: Registro de hogares")
    hogares = registrar_hogares()
    
    # Paso 2: Validar y mostrar estado de cada hogar
    print("\n>> FASE 2: Validación de hogares")
    i = 0
    while i < len(hogares):
        hogar = hogares[i]
        es_valido = validar_hogar(hogar)
        estado = "VÁLIDO" if es_valido else "NO VÁLIDO"
        print("Hogar " + str(i + 1) + " (" + hogar["responsable"] + "): " + estado)
        i = i + 1
    
    # Paso 3: Calcular puntajes y prioridades
    print("\n>> FASE 3: Cálculo de puntajes y prioridades")
    i = 0
    while i < len(hogares):
        hogar = hogares[i]
        es_valido = validar_hogar(hogar)
        
        if es_valido:
            puntaje = calcular_puntaje(hogar)
            prioridad = clasificar_prioridad(puntaje)
            print("Hogar " + str(i + 1) + " (" + hogar["responsable"] + "): Puntaje=" + str(puntaje) + ", Prioridad=" + prioridad)
        else:
            print("Hogar " + str(i + 1) + " (" + hogar["responsable"] + "): No válido (sin puntaje)")
        
        i = i + 1
    
    # Paso 4: Registrar entregas
    print("\n>> FASE 4: Registro de entregas")
    hogares = registrar_entregas(hogares)
    
    # Paso 5: Generar resumen final
    print("\n>> FASE 5: Resumen final")
    generar_resumen(hogares)
    
    print("\nPrograma finalizado.")


# Ejecución del programa
if __name__ == "__main__":
    main()