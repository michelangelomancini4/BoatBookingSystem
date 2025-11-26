from agendmanager import AgendManager
from client import Client
from service import Service

def main():
    agend_manager = AgendManager()

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

    # show
    agend_manager.show_client()  
    print()
    agend_manager.show_services()

if __name__ == "__main__":
    main()
