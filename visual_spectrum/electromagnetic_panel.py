import tkinter as tk
from induction_core.particle import Particle
from induction_core.double_circuit import DoubleCircuit

class ElectromagneticPanel:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Musical Spectrum - Electromagnetic Panel")
        self.root.geometry("800x600")
        self.root.configure(bg="black")
        
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.particles = [Particle(self.canvas) for _ in range(30)]
        self.circuit = DoubleCircuit(self.canvas)
        
        self.update()

    def update(self):
        # Update logic
        for p in self.particles:
            p.move()
        
        self.circuit.pulse()
        
        # Animation loop
        self.root.after(50, self.update)

    def activate(self):
        print("Electromagnetic panel activated. Energy flowing.")
        self.root.mainloop()