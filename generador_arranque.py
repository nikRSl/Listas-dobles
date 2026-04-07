import sys
import os

# Añadir el directorio actual al path para las importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from espectro_visual.panel_electromagnetico import PanelElectromagnetico

def iniciar_secuencia():
    print("Iniciando Generador de Arranque...")
    panel = PanelElectromagnetico()
    panel.activar()

if __name__ == "__main__":
    iniciar_secuencia()