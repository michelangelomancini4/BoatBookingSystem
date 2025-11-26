from datetime import datetime

class Booking:
    def __init__(self, client, service, date_time):
        """
        data_ora: oggetto datetime
        """
        self.client = client
        self.service = service
        self.date_time = date_time

    def __str__(self):
        data_str = self.date_time.strftime("%d/%m/%Y %H:%M")
        return f"{data_str} - {self.client.name} → {self.service.nome}"
