import os
import shutil
import sys
import io
import argparse
import subprocess
from pathlib import Path
import xml.etree.ElementTree as ET

# --- FIX WINDOWS ---
# Forzar salida UTF-8 para evitar errores de consola en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# --- CONFIGURACION ---
# Ajusta esta ruta si tu draw.io está en otro lado
DRAWIO_PATH = r"C:\Program Files\draw.io\draw.io.exe"
PROJECT_ROOT = "."
# Carpetas que el script ignorará
IGNORE_DIRS = {'.git', '.venv', '_site', '.quarto', 'site_libs'}

def get_output_dir(drawio_path):
    """Calcula la ruta de salida basada en la ubicación del archivo .drawio"""
    path_obj = Path(drawio_path)
    stem_name = path_obj.stem 
    # Sube dos niveles asumiendo estructura: carpeta/assets/archivo.drawio
    # Destino: carpeta/images/archivo/
    section_root = path_obj.parent.parent 
    final_dir = section_root / "images" / stem_name
    return final_dir

def analyze_drawio_pages(filepath):
    """Detecta cuantas pestañas tiene el archivo"""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        diagrams = root.findall('diagram')
        pages_map = {}
        for i in range(len(diagrams)):
            # Nombres secuenciales: 01.webp, 02.webp...
            filename = f"{i+1:02d}.webp"
            pages_map[i] = filename
        return pages_map
    except Exception:
        return {}

def generate_images(filepath):
    """Genera las imagenes usando draw.io CLI"""
    filepath = Path(filepath)
    output_dir = get_output_dir(filepath)
    
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"[Creando] {output_dir}")

    pages_map = analyze_drawio_pages(filepath)
    if not pages_map: return

    for page_idx, filename in pages_map.items():
        output_file = output_dir / filename
        
        # Cache simple: si el drawio es mas viejo que la imagen, saltar
        if output_file.exists() and output_file.stat().st_mtime > filepath.stat().st_mtime:
            continue 

        cmd = [
            DRAWIO_PATH, 
            "-x",               # Exportar
            "-f", "webp",       # Formato WebP
            "-t",               # Transparente
            "-b", "0",          # Borde 0
            "-s", "2",          # Escala 2 (HD ligero)
            "-p", str(page_idx),
            "-o", str(output_file), 
            str(filepath)
        ]
        try:
            subprocess.run(cmd, capture_output=True)
            print(f"  -> Generado: {output_file.name}")
        except Exception as e:
            print(f"  [Error] {e}")

def clean_images(filepath):
    """Elimina la carpeta de imagenes generada para este archivo"""
    filepath = Path(filepath)
    output_dir = get_output_dir(filepath)
    
    if output_dir.exists() and output_dir.is_dir():
        try:
            shutil.rmtree(output_dir)
            print(f"[Limpieza] Borrada carpeta: {output_dir}")
            
            # Opcional: Si la carpeta padre 'images' queda vacía, borrarla también
            parent_images = output_dir.parent
            if parent_images.exists() and not any(parent_images.iterdir()):
                parent_images.rmdir()
                print(f"[Limpieza] Borrada carpeta vacia: {parent_images}")
                
        except Exception as e:
            print(f"[Error Limpieza] {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true', help='Borrar imagenes generadas en lugar de crear')
    args = parser.parse_args()

    action_name = "Limpieza" if args.clean else "Generacion"
    print(f"--- Iniciando {action_name} de diagramas ---")
    
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Filtrar carpetas ignoradas
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if file.endswith(".drawio"):
                full_path = os.path.join(root, file)
                if args.clean:
                    clean_images(full_path)
                else:
                    generate_images(full_path)

    print(f"--- {action_name} finalizada ---")

if __name__ == "__main__":
    main()