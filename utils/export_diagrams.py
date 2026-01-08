import os
import subprocess
import sys
import io
import xml.etree.ElementTree as ET

# --- FIX PARA WINDOWS/QUARTO ---
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# --- CONFIGURACION ---
DRAWIO_PATH = r"C:\Program Files\draw.io\draw.io.exe"
SOURCE_FILE = "assets/diagrams/master.drawio"
OUTPUT_DIR = "images/generated/"

def analyze_drawio_pages(filepath):
    """
    Lee el archivo XML de draw.io y devuelve un diccionario automático
    con indices y nombres secuenciales (01.png, 02.png...)
    """
    try:
        # Parseamos el archivo XML
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        # En draw.io, cada pestaña está dentro de una etiqueta <diagram>
        diagrams = root.findall('diagram')
        
        total_pages = len(diagrams)
        print(f"[Info] Se detectaron {total_pages} pestañas en el archivo.")
        
        pages_map = {}
        for i in range(total_pages):
            # Generamos nombre: 01.png, 02.png, etc.
            # {:02d} asegura que el numero tenga 2 digitos (rellena con cero)
            filename = f"{i+1:02d}.png" 
            pages_map[i] = filename
            
        return pages_map

    except Exception as e:
        print(f"[Error XML] No se pudo leer la estructura del archivo drawio: {e}")
        return {}

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"[Info] Carpeta creada: {OUTPUT_DIR}")

    if not os.path.exists(SOURCE_FILE):
        print(f"[Error] No se encuentra el archivo origen: {SOURCE_FILE}")
        return

    # --- GENERACION AUTOMATICA DEL MAPA ---
    pages_map = analyze_drawio_pages(SOURCE_FILE)

    if not pages_map:
        print("[Alerta] No hay paginas para exportar o el archivo esta vacio.")
        return

    print(f"[Info] Iniciando exportacion automatica...")

    for page_idx, filename in pages_map.items():
        output_path = os.path.join(OUTPUT_DIR, filename)
        
        cmd = [
            DRAWIO_PATH,
            "-x",               # Exportar
            "-f", "png",        # Formato
            "-t",               # Transparent
            "-b", "0",          # Borde 0
            "-s", "2",          # Scale 2 (200% Zoom)
            "-p", str(page_idx),# Pagina
            "-o", output_path,  # Salida
            SOURCE_FILE         # Entrada
        ]

        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True,
                encoding='utf-8' 
            )
            
            if result.returncode == 0:
                print(f"  [OK] Pagina {page_idx} -> {filename}")
            else:
                print(f"  [Error] Fallo exportacion de pag {page_idx}")
                
        except Exception as e:
            print(f"  [Excepcion] {e}")

if __name__ == "__main__":
    main()