import tkinter as tk
from nucleo_induccion.particula import Particula
from nucleo_induccion.circuito_doble import CircuitoDoble

class PanelElectromagnetico:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Espectro Musical - Panel Electromagnético")
        self.root.geometry("800x600")
        self.root.configure(bg="black")
        
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.particulas = [Particula(self.canvas) for _ in range(30)]
        self.circuito = CircuitoDoble(self.canvas)
        
        self.actualizar()

    def actualizar(self):
        # Actualizar lógica
        for p in self.particulas:
            p.mover()
        
        self.circuito.pulsar()
        
        # Bucle de animación
        self.root.after(50, self.actualizar)

    def activar(self):
        print("Panel electromagnético activado. Energía fluyendo.")
        self.root.mainloop()