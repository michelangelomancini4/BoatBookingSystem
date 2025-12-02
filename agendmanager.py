from client import Client
from service import Service
from booking import Booking

from datetime import datetime
import json
from pathlib import Path

DATA_FILE = Path("agenda_data.json")

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

    # ---------- PERSISTENCE (SAVE / LOAD) ----------

    def to_dict(self):
        """Convert current state to a serializable dict (for JSON)."""
        return {
            "clients": [
                {
                    "client_id": c.client_id,
                    "name": c.name,
                    "telephone": c.telephone,
                    "email": c.email,
                }
                for c in self.clients
            ],
            "services": [
                {
                    "name": s.name,
                    "duration": s.duration,
                    "price": s.price,
                }
                for s in self.services
            ],
            "bookings": [
                {
                    "client_id": b.client.client_id,
                    "service_name": b.service.name,
                    "date_time": b.date_time.strftime("%Y-%m-%d %H:%M"),
                }
                for b in self.bookings
            ],
        }

    def save_to_file(self, path: Path = DATA_FILE):
        data = self.to_dict()
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"💾 Data saved to {path}")

    def load_from_file(self, path: Path = DATA_FILE):
        if not path.exists():
            print("No data file found, starting with empty agenda.")
            return

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # clear current lists
        self.clients = []
        self.services = []
        self.bookings = []

        # recreate clients
        from client import Client
        from service import Service

        id_to_client = {}

        for c in data.get("clients", []):
            client = Client(
                c["client_id"],
                c["name"],
                telephone=c.get("telephone"),
                email=c.get("email"),
            )
            self.clients.append(client)
            id_to_client[client.client_id] = client

        name_to_service = {}

        for s in data.get("services", []):
            service = Service(
                s["name"],
                s["duration"],
                s["price"],
            )
            self.services.append(service)
            name_to_service[service.name] = service

        for b in data.get("bookings", []):
            client = id_to_client.get(b["client_id"])
            service = name_to_service.get(b["service_name"])
            if client is None or service is None:
                continue  # skip invalid booking

            date_time = datetime.strptime(b["date_time"], "%Y-%m-%d %H:%M")
            booking = Booking(client, service, date_time)
            self.bookings.append(booking)

        print(f"✅ Data loaded from {path}")