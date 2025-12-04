class ClientNotFoundError(Exception):
    """Raised when a client is not found."""
    pass

class ServiceNotFoundError(Exception):
    """Raised when a service is not found."""
    pass

class BookingNotFoundError(Exception):
    """Raised when a booking is not found."""
    pass

class InvalidDateError(Exception):
    """Raised when a date is invalid or in the past."""
    pass

class InvalidServiceDataError(Exception):
    """Raised when service data (price, duration, name) is invalid."""
    pass

class InvalidClientDataError(Exception):
    """Raised when client data (name, email, phone) is invalid."""
    pass
