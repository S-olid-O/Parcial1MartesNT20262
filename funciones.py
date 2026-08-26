# =============================================================================
# BANCO DE ALIMENTOS - MEDELLÍN
# Archivo: funciones.py
# Contiene las 6 funciones obligatorias del ejercicio
# =============================================================================

def registrar_hogares():
    """
    Solicitar y registrar 12 hogares. Cada hogar se almacena como diccionario.
    Retorna la lista completa de hogares.
    """
    hogares = []
    
    i = 0
    while i < 12:
        print("\n--- Registro de hogar #" + str(i + 1) + " ---")
        
        documento = input("Documento del responsable: ")
        responsable = input("Nombre completo del responsable: ")
        barrio = input("Barrio de residencia: ")
        
        # Lectura de valores numéricos
        integrantes = int(input("Cantidad de personas del hogar: "))
        menores = int(input("Cantidad de menores de edad: "))
        adultos_mayores = int(input("Cantidad de adultos mayores: "))
        ingreso_mensual = float(input("Ingreso mensual estimado del hogar: "))
        
        hogar = {
            "documento": documento,
            "responsable": responsable,
            "barrio": barrio,
            "integrantes": integrantes,
            "menores": menores,
            "adultos_mayores": adultos_mayores,
            "ingreso_mensual": ingreso_mensual,
            "entregado": False
        }
        
        hogares.append(hogar)
        i = i + 1
    
    return hogares


def validar_hogar(hogar):
    """
    Validar que:
    - integrantes sea mayor que 0
    - menores y adultos_mayores no sean negativos
    - la suma de menores y adultos mayores no supere integrantes
    - el ingreso mensual no sea negativo
    Retorna True o False.
    """
    integrantes = hogar["integrantes"]
    menores = hogar["menores"]
    adultos_mayores = hogar["adultos_mayores"]
    ingreso_mensual = hogar["ingreso_mensual"]
    
    if integrantes <= 0:
        return False
    
    if menores < 0:
        return False
    
    if adultos_mayores < 0:
        return False
    
    if (menores + adultos_mayores) > integrantes:
        return False
    
    if ingreso_mensual < 0:
        return False
    
    return True


def calcular_puntaje(hogar):
    """
    Calcular puntaje de vulnerabilidad:
    - +2 puntos si ingreso < 1.000.000
    - +1 si ingreso entre 1.000.000 y 2.000.000
    - +1 por cada menor (máximo 3 puntos)
    - +2 si existe al menos un adulto mayor
    - +1 si el hogar tiene 5 o más integrantes
    Retorna el puntaje.
    """
    puntaje = 0
    
    ingreso = hogar["ingreso_mensual"]
    menores = hogar["menores"]
    adultos_mayores = hogar["adultos_mayores"]
    integrantes = hogar["integrantes"]
    
    # Puntaje por ingreso
    if ingreso < 1000000:
        puntaje = puntaje + 2
    elif ingreso >= 1000000 and ingreso <= 2000000:
        puntaje = puntaje + 1
    
    # Puntaje por menores (máximo 3)
    puntos_menores = menores
    if puntos_menores > 3:
        puntos_menores = 3
    puntaje = puntaje + puntos_menores
    
    # Puntaje por adultos mayores
    if adultos_mayores >= 1:
        puntaje = puntaje + 2
    
    # Puntaje por cantidad de integrantes
    if integrantes >= 5:
        puntaje = puntaje + 1
    
    return puntaje


def clasificar_prioridad(puntaje):
    """
    Clasificar el puntaje:
    - 0–2 = Baja
    - 3–4 = Media
    - 5–6 = Alta
    - 7 o más = Urgente
    Retorna el texto de la prioridad.
    """
    if puntaje <= 2:
        return "Baja"
    elif puntaje >= 3 and puntaje <= 4:
        return "Media"
    elif puntaje >= 5 and puntaje <= 6:
        return "Alta"
    else:
        return "Urgente"


def registrar_entregas(hogares):
    """
    Recorrer los hogares y permitir marcar si el paquete fue entregado.
    Solo se puede marcar como entregado un hogar válido.
    Modifica y retorna la lista actualizada.
    """
    i = 0
    while i < len(hogares):
        hogar = hogares[i]
        
        es_valido = validar_hogar(hogar)
        
        if es_valido:
            print("\nHogar: " + hogar["responsable"] + " (Documento: " + hogar["documento"] + ")")
            respuesta = input("¿Se entregó el paquete alimentario? (s/n): ")
            
            if respuesta == "s" or respuesta == "S":
                hogares[i]["entregado"] = True
            else:
                hogares[i]["entregado"] = False
        else:
            print("\nHogar no válido (se saltea): " + hogar["responsable"])
            hogares[i]["entregado"] = False
        
        i = i + 1
    
    return hogares


def generar_resumen(hogares):
    """
    Recorrer la lista y mostrar:
    - Cantidad total de hogares válidos
    - Cuántos quedaron en cada prioridad
    - Cuántos paquetes fueron entregados
    - Cuántos están pendientes
    """
    total_validos = 0
    prioridad_baja = 0
    prioridad_media = 0
    prioridad_alta = 0
    prioridad_urgente = 0
    entregados = 0
    pendientes = 0
    
    i = 0
    while i < len(hogares):
        hogar = hogares[i]
        
        es_valido = validar_hogar(hogar)
        
        if es_valido:
            total_validos = total_validos + 1
            
            puntaje = calcular_puntaje(hogar)
            prioridad = clasificar_prioridad(puntaje)
            
            if prioridad == "Baja":
                prioridad_baja = prioridad_baja + 1
            elif prioridad == "Media":
                prioridad_media = prioridad_media + 1
            elif prioridad == "Alta":
                prioridad_alta = prioridad_alta + 1
            elif prioridad == "Urgente":
                prioridad_urgente = prioridad_urgente + 1
            
            if hogar["entregado"]:
                entregados = entregados + 1
            else:
                pendientes = pendientes + 1
        
        i = i + 1
    
    print("\n" + "=" * 50)
    print("RESUMEN DEL BANCO DE ALIMENTOS")
    print("=" * 50)
    print("Total de hogares válidos: " + str(total_validos))
    print("")
    print("Distribución por prioridad:")
    print("  - Baja: " + str(prioridad_baja))
    print("  - Media: " + str(prioridad_media))
    print("  - Alta: " + str(prioridad_alta))
    print("  - Urgente: " + str(prioridad_urgente))
    print("")
    print("Estado de entregas:")
    print("  - Paquetes entregados: " + str(entregados))
    print("  - Paquetes pendientes: " + str(pendientes))
    print("=" * 50)