# ACDA 1 - Evaluación de Python Básico

## Para enviarlo:
https://forms.gle/NtTbgGCyLRtAD2mp6

## Caso 1: Sistema de priorización de entregas para un banco de alimentos

## Contexto
Un banco de alimentos de Medellín recibe solicitudes de apoyo de familias afectadas por situaciones económicas temporales. Actualmente, el equipo registra la información de manera manual y necesita una solución básica que permita organizar las solicitudes, estimar la prioridad de atención y controlar la entrega de paquetes alimentarios.

## Reto
Desarrolle un programa en Python que resuelva el caso planteado. La solución debe estar dividida en **exactamente 6 funciones principales**, descritas a continuación.

## Estructura de los datos
Cada registro principal debe representarse mediante un **diccionario** y almacenarse en una **lista**.

- **documento**: Documento del responsable del hogar.
- **responsable**: Nombre completo.
- **barrio**: Barrio de residencia.
- **integrantes**: Cantidad de personas del hogar.
- **menores**: Cantidad de menores de edad.
- **adultos_mayores**: Cantidad de adultos mayores.
- **ingreso_mensual**: Ingreso mensual estimado del hogar.
- **entregado**: Estado de entrega: inicialmente False.

## Funciones obligatorias

### 1. registrar_hogares()
Solicitar y registrar 12 hogares. Cada hogar debe almacenarse como un diccionario y todos los hogares deben quedar en una lista. La función retorna la lista completa.

### 2. validar_hogar(hogar)
Validar que integrantes sea mayor que 0, que menores y adultos_mayores no sean negativos, que la suma de menores y adultos mayores no supere la cantidad de integrantes y que el ingreso mensual no sea negativo. Retorna True o False.

### 3. calcular_puntaje(hogar)
Calcular un puntaje de vulnerabilidad: +2 puntos si el ingreso es menor de $1.000.000; +1 si está entre $1.000.000 y $2.000.000; +1 por cada menor (máximo 3 puntos); +2 si existe al menos un adulto mayor; +1 si el hogar tiene 5 o más integrantes. Retorna el puntaje.

### 4. clasificar_prioridad(puntaje)
Clasificar el puntaje: 0–2 = Baja, 3–4 = Media, 5–6 = Alta, 7 o más = Urgente. Retorna el texto de la prioridad.

### 5. registrar_entregas(hogares)
Recorrer los hogares y permitir marcar si el paquete fue entregado. Solo se puede marcar como entregado un hogar válido. La función modifica/retorna la lista actualizada.

### 6. generar_resumen(hogares)
Recorrer la lista y mostrar: cantidad total de hogares válidos, cuántos quedaron en cada prioridad, cuántos paquetes fueron entregados y cuántos están pendientes.

## Restricciones técnicas
- No utilizar clases, archivos, bases de datos, librerías externas, comprensión de listas ni funciones avanzadas.
- La solución debe construirse únicamente con funciones, ciclos, condicionales, listas, diccionarios, variables y operaciones básicas.
- Cada función debe cumplir una responsabilidad específica y debe ser utilizada dentro del programa principal.
- Los datos deben ser ingresados por teclado; no se acepta entregar únicamente datos quemados.
- El programa debe ejecutar un flujo completo y mostrar resultados legibles.

## Entrega esperada
- Código fuente ejecutable en Python.
- Las 6 funciones solicitadas claramente identificadas.
- Programa principal que invoque las funciones y permita comprobar el funcionamiento completo.
- Nombres de variables y funciones comprensibles.
- Salidas en consola suficientemente claras para interpretar el resultado.

> **Importante:** se evaluará tanto que el programa funcione como la forma en que el problema fue dividido y resuelto mediante funciones.
