# --- PROGRAMA DE RENDIMIENTO COSECHA (MAIN) ---

def calcular_mejor_especialista(datos_cuadrilla, fruta_objetivo):
    mejor_rendimiento = 0
    especialista_top = None

    for trabajador in datos_cuadrilla:
        if trabajador["especialidad"] == fruta_objetivo:
            if trabajador["cajas"] > mejor_rendimiento:
                mejor_rendimiento = trabajador["cajas"]
                especialista_top = trabajador
    return especialista_top

def calcular_promedio_edad(datos_cuadrilla):
    if not datos_cuadrilla:
        return 0
    total_edad = sum(t["edad"] for t in datos_cuadrilla)
    return total_edad / len(datos_cuadrilla)

# --- DATOS QUE VENDRÁN DE LAS RAMAS (Juan, Pedro, Pablo) ---

datos_temporada = [
    # Cuadrilla Juan
    {"nombre": "Andrei", "nacionalidad": "Rumano", "edad": 32, "especialidad": "Mandarina", "cajas": 45},
    {"nombre": "José", "nacionalidad": "Español", "edad": 28, "especialidad": "Limón", "cajas": 38},
    {"nombre": "Luis", "nacionalidad": "Argentino", "edad": 35, "especialidad": "Naranja", "cajas": 52},
    
    # Cuadrilla Pedro
    {"nombre": "Mateo", "nacionalidad": "Rumano", "edad": 30, "especialidad": "Mandarina", "cajas": 48},
    {"nombre": "Carlos", "nacionalidad": "Español", "edad": 42, "especialidad": "Limón", "cajas": 40},
    {"nombre": "Santi", "nacionalidad": "Uruguayo", "edad": 26, "especialidad": "Naranja", "cajas": 41},
    
    # Cuadrilla Pablo (El tercer equipo que faltaba)
    {"nombre": "Nikolai", "nacionalidad": "Rumano", "edad": 38, "especialidad": "Mandarina", "cajas": 50},
    {"nombre": "Fran", "nacionalidad": "Español", "edad": 33, "especialidad": "Limón", "cajas": 44},
    {"nombre": "Ariel", "nacionalidad": "Paraguayo", "edad": 29, "especialidad": "Naranja", "cajas": 49}
]

# --- ANÁLISIS DE RESULTADOS ---

print("--- REPORTE DE PRODUCTIVIDAD CITRUS HMN ---")

# Buscamos los mejores de cada categoría
for fruta in ["Limón", "Mandarina", "Naranja"]:
    ganador = calcular_mejor_especialista(datos_temporada, fruta)
    if ganador:
        print(f"Mejor en {fruta}: {ganador['nombre']} ({ganador['nacionalidad']}) con {ganador['cajas']} cajas.")

print("-" * 40)
promedio = calcular_promedio_edad(datos_temporada)
print(f"Promedio de edad de la fuerza de trabajo: {promedio:.1f} años")