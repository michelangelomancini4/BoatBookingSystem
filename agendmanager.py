from client import Client
from service import Service
from booking import Booking
from datetime import datetime

class AgendManager:
    def __init__(self):
        self.clients= []
        self.services= []
        self.bookings= []

    #  --- CLIENTS ---

    def add_client(self,client):
        self.clients.append(client)

    def show_clients(self):
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
      # --- HELPER METHODS ---

    def find_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def find_service_by_name(self, name):
        for service in self.services:
            if service.name.lower() == name.lower():
                return service
        return None
    # --- BOOKINGS ---

    def add_booking(self, client_id, service_name, date_time):
        client = self.find_client_by_id(client_id)
        service = self.find_service_by_name(service_name)

        if client is None:
            print(f" Client with id {client_id} not found.")
            return

        if service is None:
            print(f" Service '{service_name}' not found.")
            return

        booking = Booking(client, service, date_time)
        self.bookings.append(booking)
        print(" Booking added:", booking)

    def show_bookings(self):
        if not self.bookings:
            print("Nessuna prenotazione.")
            return

        print("Prenotazioni:")
        # le ordiniamo per data/ora
        for booking in sorted(self.bookings, key=lambda b: b.date_time):
            print("-", booking)
    