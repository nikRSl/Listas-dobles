import sys
import os

# Add the current directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from visual_spectrum.electromagnetic_panel import ElectromagneticPanel

def start_sequence():
    print("Starting Boot Generator...")
    panel = ElectromagneticPanel()
    panel.activate()

if __name__ == "__main__":
    start_sequence()