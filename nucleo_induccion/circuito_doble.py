import math

class CircuitoDoble:
    def __init__(self, canvas):
        self.canvas = canvas
        self.angulo = 0
        self.cx = 400
        self.cy = 300
        self.radio_base = 150
        
        self.id_ovalo1 = self.canvas.create_oval(
            self.cx - self.radio_base, self.cy - self.radio_base,
            self.cx + self.radio_base, self.cy + self.radio_base,
            outline="#ff0044", width=2, dash=(4, 4)
        )
        self.id_ovalo2 = self.canvas.create_oval(
            self.cx - self.radio_base*1.5, self.cy - self.radio_base*1.5,
            self.cx + self.radio_base*1.5, self.cy + self.radio_base*1.5,
            outline="#4400ff", width=2, dash=(2, 6)
        )
        
    def pulsar(self):
        self.angulo += 0.15
        escala1 = 1.0 + 0.1 * math.sin(self.angulo)
        escala2 = 1.5 + 0.1 * math.cos(self.angulo)
        
        r1 = self.radio_base * escala1
        r2 = self.radio_base * escala2
        
        self.canvas.coords(
            self.id_ovalo1,
            self.cx - r1, self.cy - r1,
            self.cx + r1, self.cy + r1
        )
        self.canvas.coords(
            self.id_ovalo2,
            self.cx - r2, self.cy - r2,
            self.cx + r2, self.cy + r2
        )