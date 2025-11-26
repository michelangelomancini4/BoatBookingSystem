class Service:
    def __init__(self, name , min_durate, price):
        self.name=name
        self.min_durate=min_durate
        self.price= price
    
    def __str__(self):
        return f"{self.name} - {self.min_durate} min - {self.price} €"