class Client:
    def __init__(self,client_id, name , telephone=None , email=None):
        self.client_id=client_id
        self.name=name
        self.telephone=telephone
        self.email=email
    
    def __str__(self):
        contatto= self.telephone or self.email or "Nessun conatto"
        return f"[{self.client_id}] {self.name} ({contatto})"