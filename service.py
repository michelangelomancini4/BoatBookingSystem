class Service:
    def __init__(self, name , duration, price):
        self.name=name
        self.duration=duration
        self.price= price
    
    def __str__(self):
        return f"{self.name} - {self.duration} min - {self.price} €"