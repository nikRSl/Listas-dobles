import random

class Particula:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)
        self.radio = random.randint(2, 6)
        self.color = random.choice(["#00ffcc", "#ff00ff", "#00ccff", "#ffff00", "#ffffff"])
        
        self.id = self.canvas.create_oval(
            self.x - self.radio, self.y - self.radio,
            self.x + self.radio, self.y + self.radio,
            fill=self.color, outline=""
        )

    def mover(self):
        self.x += self.vx
        self.y += self.vy
        
        # Rebote en los bordes
        if self.x <= 0 or self.x >= 800:
            self.vx *= -1
        if self.y <= 0 or self.y >= 600:
            self.vy *= -1
            
        self.canvas.coords(
            self.id,
            self.x - self.radio, self.y - self.radio,
            self.x + self.radio, self.y + self.radio
        )