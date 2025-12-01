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


def print_menu():
    print("\n===== Agenda Manager =====")
    print("1) Show clients")
    print("2) Show services")
    print("3) Add booking")
    print("4) Show bookings")
    print("5) Add client")
    print("6) Add service")
    print("0) Exit")


def main():
    agend_manager = AgendManager()
    seed_data(agend_manager)  # togli se non vuoi dati di test

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
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("❌ Invalid option, please try again.")


if __name__ == "__main__":
    main()
