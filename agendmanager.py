from client import Client
from service import Service
from booking import Booking

class AgendManager:
    def __init__(self):
        self.clients= []
        self.services= []
        self.bookings= []

    #  --- CLIENTS ---

    def add_client(self,client):
        self.clients.append(client)

    def show_client(self):
        if not self.clients:
            print("Nessun cliente registrato.")
            return
        print("Clienti registrati:")
        for client in self.clients:
            print("-", client)

    # --- SERVICES ---

    def add_service(self , service):
        self.services.append(service)

    def show_services(self):
        if not self.services:
            print("Nessun servizio disponibile.")
            return
        print("Servizi disponibili:")
        for service in self.services:
            print("-", service)

    