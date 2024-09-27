class Person:
    def __init__(self, name: str, auto=None):
        self.name = name
        self.auto = auto
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, Auto: {self.auto}"

class Auto:
    def __init__(self, modell: str, geschw: str, farbe: str):
        self.modell = modell
        self.geschw = geschw
        self.farbe = farbe
    def __repr__(self) -> str:
        return f"Modelle: {self.modell}, Geschwindigkeit: {self.geschw}, Farbe: {self.farbe}"