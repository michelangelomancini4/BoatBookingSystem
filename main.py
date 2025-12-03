from agendmanager import AgendManager
from client import Client
from service import Service
from datetime import datetime


def seed_data(agend_manager: AgendManager):
    """Dati di esempio per non partire a lista vuota."""
    # test names
    c1 = Client(1, "Luca Verdi", telephone="34912345678")
    c2 = Client(2, "Giuseppe Nossi", email="nossi@gin.it")

    agend_manager.add_client(c1)
    agend_manager.add_client(c2)

    # services test
    s1 = Service("Giro grotte in barca", 90, 40.0)
    s2 = Service("Tramonto in barca", 120, 60.0)

    agend_manager.add_service(s1)
    agend_manager.add_service(s2)


def create_client_interactive(agend_manager: AgendManager):
    """Crea un nuovo cliente chiedendo i dati all'utente."""
    print("\n--- Add new client ---")
    name = input("Enter client name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    telephone = input("Enter telephone (optional): ").strip()
    email = input("Enter email (optional): ").strip()

    if not telephone and not email:
        print("❌ At least one contact (telephone or email) is required.")
        return

    # genera nuovo id: max esistente + 1
    new_id = max((c.client_id for c in agend_manager.clients), default=0) + 1

    client = Client(new_id, name, telephone=telephone or None, email=email or None)
    agend_manager.add_client(client)
    print(f"✅ Client added: {client}")


def create_service_interactive(agend_manager: AgendManager):
    """Crea un nuovo servizio chiedendo i dati all'utente."""
    print("\n--- Add new service ---")
    name = input("Enter service name: ").strip()
    if not name:
        print("❌ Service name cannot be empty.")
        return

    duration_str = input("Enter duration in minutes: ").strip()
    if not duration_str.isdigit():
        print("❌ Duration must be a number of minutes.")
        return
    duration = int(duration_str)

    price_str = input("Enter price (e.g. 40 or 40.0): ").strip()
    try:
        price = float(price_str)
    except ValueError:
        print("❌ Price must be a number.")
        return

    service = Service(name, duration, price)
    agend_manager.add_service(service)
    print(f"✅ Service added: {service}")


def create_booking_interactive(agend_manager: AgendManager):
    """Crea una prenotazione chiedendo i dati all'utente."""
    print("\n--- Create new booking ---")
    agend_manager.show_clients()
    print()
    agend_manager.show_services()
    print()

    # scegli client
    client_id_input = input("Enter client id: ").strip()
    if not client_id_input.isdigit():
        print("❌ Invalid client id.")
        return
    client_id = int(client_id_input)

    # scegli service
    service_name = input("Enter service name (exact): ").strip()
    if not service_name:
        print("❌ Service name cannot be empty.")
        return

    # scegli data/ora
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ").strip()
    try:
        date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD HH:MM.")
        return

    agend_manager.add_booking(client_id, service_name, date_time)

# ---UPDATE SECTION----
# CLIENT
def update_client_interactive(agend_manager: AgendManager):
    print("\n--- Update client ---")
    agend_manager.show_clients()
    if not agend_manager.clients:
        return

    client_id_input = input("Enter client id to update: ").strip()
    if not client_id_input.isdigit():
        print("❌ Invalid client id.")
        return

    client_id = int(client_id_input)
    client = agend_manager.find_client_by_id(client_id)
    if client is None:
        print(f"❌ Client with id {client_id} not found.")
        return

    print(f"Current name: {client.name}")
    new_name = input("New name (press Enter to keep): ").strip()
    if new_name == "":
        new_name = None

    print(f"Current telephone: {client.telephone}")
    new_tel = input("New telephone (press Enter to keep): ").strip()
    if new_tel == "":
        new_tel = None

    print(f"Current email: {client.email}")
    new_email = input("New email (press Enter to keep): ").strip()
    if new_email == "":
        new_email = None

    agend_manager.update_client(client_id, name=new_name, telephone=new_tel, email=new_email)
# SERVICE
def update_service_interactive(agend_manager: AgendManager):
    print("\n--- Update service ---")
    agend_manager.show_services()
    if not agend_manager.services:
        return

    name = input("Enter current service name to update: ").strip()
    if not name:
        print("❌ Service name cannot be empty.")
        return

    service = agend_manager.find_service_by_name(name)
    if service is None:
        print(f"❌ Service '{name}' not found.")
        return

    print(f"Current name: {service.name}")
    new_name = input("New name (press Enter to keep): ").strip()
    if new_name == "":
        new_name = None

    print(f"Current duration (minutes): {service.duration}")
    duration_str = input("New duration (press Enter to keep): ").strip()
    if duration_str == "":
        new_duration = None
    elif duration_str.isdigit():
        new_duration = int(duration_str)
    else:
        print("❌ Duration must be a number or empty.")
        return

    print(f"Current price: {service.price}")
    price_str = input("New price (press Enter to keep): ").strip()
    if price_str == "":
        new_price = None
    else:
        try:
            new_price = float(price_str)
        except ValueError:
            print("❌ Price must be a number or empty.")
            return

    agend_manager.update_service(name, new_name=new_name, new_duration=new_duration, new_price=new_price)
# BOOKING

def update_booking_interactive(agend_manager: AgendManager):
    print("\n--- Update booking ---")
    agend_manager.show_bookings()
    if not agend_manager.bookings:
        return

    index_input = input("Enter booking number to update: ").strip()
    if not index_input.isdigit():
        print("❌ Invalid booking number.")
        return

    index = int(index_input)
    if index < 1 or index > len(agend_manager.bookings):
        print("❌ Invalid booking number.")
        return

    booking = agend_manager.bookings[index - 1]
    print(f"Current booking: {booking}")

    # cambio servizio (opzionale)
    change_service = input("Change service? (y/N): ").strip().lower()
    new_service_name = None
    if change_service == "y":
        agend_manager.show_services()
        new_service_name = input("Enter new service name (exact): ").strip()
        if not new_service_name:
            print("❌ Service name cannot be empty.")
            return

    # cambio data (opzionale)
    from datetime import datetime
    print(f"Current date/time: {booking.date_time.strftime('%Y-%m-%d %H:%M')}")
    date_str = input("New date/time (YYYY-MM-DD HH:MM, Enter to keep): ").strip()
    if date_str == "":
        new_date_time = None
    else:
        try:
            new_date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("❌ Invalid date format.")
            return

    agend_manager.update_booking(index, new_service_name=new_service_name, new_date_time=new_date_time)

# ---DELETE SECTION-----

def delete_client_interactive(agend_manager: AgendManager):
    print("\n--- Delete client ---")
    agend_manager.show_clients()
    if not agend_manager.clients:
        return

    client_id_input = input("Enter client id to delete: ").strip()
    if not client_id_input.isdigit():
        print("❌ Invalid client id.")
        return

    client_id = int(client_id_input)
    agend_manager.delete_client(client_id)

def delete_service_interactive(agend_manager: AgendManager):
    print("\n--- Delete service ---")
    agend_manager.show_services()
    if not agend_manager.services:
        return

    name = input("Enter service name to delete (exact): ").strip()
    if not name:
        print("❌ Service name cannot be empty.")
        return

    agend_manager.delete_service(name)

def delete_booking_interactive(agend_manager: AgendManager):
    print("\n--- Delete booking ---")
    agend_manager.show_bookings()
    if not agend_manager.bookings:
        return

    index_input = input("Enter booking number to delete: ").strip()
    if not index_input.isdigit():
        print("❌ Invalid booking number.")
        return

    index = int(index_input)
    agend_manager.delete_booking(index)




def print_menu():
    print("\n===== Agenda Manager =====")
    print("1) Show clients")
    print("2) Show services")
    print("3) Add booking")
    print("4) Show bookings")
    print("5) Add client")
    print("6) Add service")
    print("7) Save data")
    print("8) Delete client")
    print("9) Delete service")
    print("10) Delete booking")
    print("11) Update client")
    print("12) Update service")
    print("13) Update booking")
    print("14) Show bookings by client")

    print("0) Exit")


def main():
    agend_manager = AgendManager()

    # prova a caricare i dati da file
    agend_manager.load_from_file()

    # usa seed_data solo se non ci sono clienti (prima esecuzione)
    if not agend_manager.clients:
        seed_data(agend_manager)
    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            agend_manager.show_clients()
        elif choice == "2":
            agend_manager.show_services()
        elif choice == "3":
            create_booking_interactive(agend_manager)
        elif choice == "4":
            agend_manager.show_bookings()
        elif choice == "5":
            create_client_interactive(agend_manager)
        elif choice == "6":
            create_service_interactive(agend_manager)
        elif choice == "7":
            agend_manager.save_to_file()
        elif choice == "8":
            delete_client_interactive(agend_manager)
        elif choice == "9":
            delete_service_interactive(agend_manager)
        elif choice == "10":
            delete_booking_interactive(agend_manager)
        elif choice == "11":
            update_client_interactive(agend_manager)
        elif choice == "12":
            update_service_interactive(agend_manager)
        elif choice == "13":
            update_booking_interactive(agend_manager)
        elif choice == "14":
            client_id_input = input("Enter client ID: ").strip()
            if client_id_input.isdigit():
                agend_manager.show_bookings_by_client(int(client_id_input))
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("❌ Invalid option, please try again.")


if __name__ == "__main__":
    main()
