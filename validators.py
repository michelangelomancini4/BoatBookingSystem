from datetime import datetime

def parse_datetime(value: str):
    try:
        date_time = datetime.strptime(value, "%Y-%m-%d %H:%M")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD HH:MM.")
        return None
def parse_int(value: str):
    """Converte una stringa in int. Ritorna None se non è valido."""
    try:
        return int(value)
    except ValueError:
        print("❌ Devi inserire un numero intero (es. 1, 2, 3).")
        return None


def parse_float(value: str):
    """Converte una stringa in float. Ritorna None se non è valido."""
    try:
        return float(value)
    except ValueError:
        print("❌ Price must be a valid number (e.g. 40 or 40.0).")
        return None
    
def validate_contact(telephone: str | None, email: str | None) -> bool:
    """
    Controlla che ci sia almeno un contatto valido (telefono o email).
    Ritorna True se va bene, False se mancano entrambi.
    """
    tel = (telephone or "").strip()
    mail = (email or "").strip()

    if tel or mail:
        return True

    print("❌ At least one contact (telephone or email) is required.")
    return False


