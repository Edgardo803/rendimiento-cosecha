import json
import os
from fpdf import FPDF

# 1. FUNCIÓN DE CARGA (La que te daba el error)
def cargar_datos():
    todos_los_trabajadores = []
    ruta_carpeta = "cuadrillas/"
    if os.path.exists(ruta_carpeta):
        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith(".json"):
                with open(os.path.join(ruta_carpeta, archivo), "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    todos_los_trabajadores.extend(datos)
    return todos_los_trabajadores

# 2. FUNCIÓN DE LÓGICA
def calcular_mejor_especialista(todos_los_datos, fruta_objetivo):
    mejor_rendimiento = 0
    especialista_top = None
    for trabajador in todos_los_datos:
        if trabajador["especialidad"] == fruta_objetivo:
            if trabajador["cajas"] > mejor_rendimiento:
                mejor_rendimiento = trabajador["cajas"]
                especialista_top = trabajador
    return especialista_top

# 3. FUNCIÓN DEL PDF
def generar_pdf_reporte(datos, ganadores, promedio_edad):
    from fpdf.enums import XPos, YPos # Importante agregar esto
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    
    # Título - Usando la nueva sintaxis para evitar avisos
    pdf.cell(190, 10, "REPORTE DE PRODUCTIVIDAD CITRUS HMN", 
             new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(10)
    
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(190, 10, "EQUIPO DE ELITE SELECCIONADO:", 
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("helvetica", "", 11)
    
    for fruta, g in ganadores.items():
        texto = f"- Mejor en {fruta}: {g['nombre']} | Edad: {g['edad']} | Nac: {g['nacionalidad']} | Cajas: {g['cajas']}"
        # Limpieza de caracteres especiales para evitar errores de codificación
        texto_limpio = texto.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(190, 8, texto_limpio, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(10)
    pdf.set_font("helvetica", "I", 10)
    pdf.cell(190, 10, f"Promedio de edad de la fuerza de trabajo: {promedio_edad:.1f} años", 
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.output("Reporte_Cosecha.pdf")
    print("\n[OK] Reporte generado: Reporte_Cosecha.pdf")

# --- EJECUCIÓN PRINCIPAL ---
datos_temporada = cargar_datos()

if not datos_temporada:
    print("No se encontraron datos en la carpeta cuadrillas/.")
else:
    ganadores_dict = {}
    for fruta in ["Limón", "Mandarina", "Naranja"]:
        ganador = calcular_mejor_especialista(datos_temporada, fruta)
        if ganador:
            ganadores_dict[fruta] = ganador
    
    promedio = sum(t["edad"] for t in datos_temporada) / len(datos_temporada)
    generar_pdf_reporte(datos_temporada, ganadores_dict, promedio)