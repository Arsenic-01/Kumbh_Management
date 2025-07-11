from db_config import get_db_connection

class LodgingReservation:
    def view_lodges(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM lodging")
        lodges = cursor.fetchall()

        print("\n--- Available Lodges ---")
        for lodge in lodges:
            print(f"{lodge[0]}. {lodge[1]} - {lodge[2]} - ₹{lodge[3]} - Rooms: {lodge[4]}")
        
        cursor.close()
        connection.close()

    def reserve_lodge(self):
        self.view_lodges()
        lodge_id = int(input("Enter Lodge ID to reserve: "))
        name = input("Enter your name: ")
        id_proof = input("Enter your ID proof: ")
        checkin = input("Enter check-in date (YYYY-MM-DD): ")
        checkout = input("Enter check-out date (YYYY-MM-DD): ")

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT available_rooms FROM lodging WHERE id = %s", (lodge_id,))
        result = cursor.fetchone()
        if result and result[0] > 0:
            cursor.execute("""
                INSERT INTO lodging_reservations (name, id_proof, lodge_id, checkin_date, checkout_date)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, id_proof, lodge_id, checkin, checkout))
            
            cursor.execute("UPDATE lodging SET available_rooms = available_rooms - 1 WHERE id = %s", (lodge_id,))
            connection.commit()
            print("✅ Lodge reserved successfully!")
        else:
            print("❌ No rooms available.")

        cursor.close()
        connection.close()
