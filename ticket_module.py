from db_config import get_db_connection
from datetime import datetime

class TicketReservation:
    def __init__(self):
        self.ticket_types = {
            "General": 100,
            "VIP": 50,
            "Seva Darshan": 30
        }

    def book_ticket(self):
        print("\n--- Ticket Booking ---")
        name = input("Enter your name: ")
        id_proof = input("Enter your ID proof (Aadhar/PAN): ")

        print("\nAvailable Ticket Types:")
        for key in self.ticket_types:
            print(f"- {key}")
        ticket_type = input("Enter ticket type: ")

        if ticket_type not in self.ticket_types:
            print("❌ Invalid ticket type.")
            return

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO tickets (name, id_proof, ticket_type, booking_time)
            VALUES (%s, %s, %s, %s)
        """
        values = (name, id_proof, ticket_type, datetime.now())

        cursor.execute(query, values)
        connection.commit()
        ticket_id = cursor.lastrowid  # Get the auto-generated ticket ID

        print("\n✅ Ticket booked successfully!")
        print("🎫 Ticket Details:")
        print(f"Ticket ID   : {ticket_id}")
        print(f"Name        : {name}")
        print(f"ID Proof    : {id_proof}")
        print(f"Ticket Type : {ticket_type}")
        print(f"Booked At   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        cursor.close()
        connection.close()

    def view_ticket(self):
        print("\n--- View Ticket Details ---")
        ticket_id = input("Enter Ticket ID: ")

        connection = get_db_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM tickets WHERE id = %s"
        cursor.execute(query, (ticket_id,))
        ticket = cursor.fetchone()

        if ticket:
            print("\n🎫 Ticket Information:")
            print(f"Ticket ID   : {ticket[0]}")
            print(f"Name        : {ticket[1]}")
            print(f"ID Proof    : {ticket[2]}")
            print(f"Ticket Type : {ticket[3]}")
            print(f"Booked At   : {ticket[4].strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("❌ No ticket found with that ID.")

        cursor.close()
        connection.close()
