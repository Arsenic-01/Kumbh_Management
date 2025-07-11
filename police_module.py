from db_config import get_db_connection
from datetime import datetime

class PoliceHelpline:
    def report_incident(self):
        print("\n--- Police Helpline ---")
        name = input("Enter your name: ")
        incident_type = input("Type of incident (Theft/Missing/etc.): ")
        description = input("Describe the incident: ")

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO police_reports (reporter_name, incident_type, description, report_time)
            VALUES (%s, %s, %s, %s)
        """, (name, incident_type, description, datetime.now()))
        connection.commit()

        print("✅ Incident reported to police.")
        cursor.close()
        connection.close()
