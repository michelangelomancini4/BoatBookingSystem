# BoatBookingSystem

## Overview

BoatBookingSystem is a simple and extensible console-based reservation manager designed for small boat tour services.  
It allows operators to register customers, define available services (tours), and handle reservations in an organized and structured way.

The project is written in Python and uses an object-oriented architecture to keep the code modular, maintainable, and easy to expand.  
Data can be persisted using JSON files (optional steps).

Although built as a learning project, the structure makes it suitable as a foundation for real-world scenarios such as coastal tours, caves excursions, kayak rentals, or any small reservation-based activity.

## Features

- Register new customers
- Register available boat tours or services
- Create reservations linking customer, service, and date/time
- Display lists of customers, services, and reservations
- Prevent double bookings for the same time slot
- Basic search and filtering (by date or customer)
- JSON-based saving and loading of data (optional final step)

## Project Structure

BoatBookingSystem/
│
├── main.py
├── cliente.py
├── servizio.py
├── prenotazione.py
├── agenda.py
└── README.md



- **cliente.py**  
  Contains the `Cliente` class, representing a registered customer.

- **servizio.py**  
  Contains the `Servizio` class, representing a boat tour or available service.

- **prenotazione.py**  
  Contains the `Prenotazione` class, which links customer, service and date/time.

- **agenda.py**  
  Contains the `Agenda` class, responsible for managing customers, services and reservations.

- **main.py**  
  Entry point of the application. Handles user interaction and menu logic.

## Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- JSON for optional data persistence  

## How to Run

1. Clone the repository:  
git clone https://github.com/<your-username>/BoatBookingSystem.git

text

2. Enter the project folder:  
cd BoatBookingSystem

text

3. Run the main script:  
python main.py



## Future Improvements

- Add validation for date and time inputs
- Add cost calculations per service
- Implement a simple graphical interface or convert to API with FastAPI
- Add customer search and pagination
- Integrate automated reminders (email/SMS)

## Purpose

This project has been developed as a learning exercise focused on clean object-oriented architecture and practical problem-solving.  
Its structure makes it a strong base for real-world small business applications, especially in the tourism sector.
