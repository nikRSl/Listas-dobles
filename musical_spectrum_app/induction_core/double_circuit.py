import math

class DoubleCircuit:
    def __init__(self, canvas):
        self.canvas = canvas
        self.angle = 0
        self.cx = 400
        self.cy = 300
        self.base_radius = 150
        
        self.id_oval1 = self.canvas.create_oval(
            self.cx - self.base_radius, self.cy - self.base_radius,
            self.cx + self.base_radius, self.cy + self.base_radius,
            outline="#ff0044", width=2, dash=(4, 4)
        )
        self.id_oval2 = self.canvas.create_oval(
            self.cx - self.base_radius*1.5, self.cy - self.base_radius*1.5,
            self.cx + self.base_radius*1.5, self.cy + self.base_radius*1.5,
            outline="#4400ff", width=2, dash=(2, 6)
        )
        
    def pulse(self):
        self.angle += 0.15
        scale1 = 1.0 + 0.1 * math.sin(self.angle)
        scale2 = 1.5 + 0.1 * math.cos(self.angle)
        
        r1 = self.base_radius * scale1
        r2 = self.base_radius * scale2
        
        self.canvas.coords(
            self.id_oval1,
            self.cx - r1, self.cy - r1,
            self.cx + r1, self.cy + r1
        )
        self.canvas.coords(
            self.id_oval2,
            self.cx - r2, self.cy - r2,
            self.cx + r2, self.cy + r2
        )