from db_config import get_db_connection
from datetime import datetime

class PublicHelpline:
    def show_menu(self):
        print("\n--- Public Helpline ---")
        print("1. Lost & Found")
        print("2. Medical Emergency")
        print("3. Information Center")
        choice = input("Choose option: ")
        issue_map = {"1": "Lost & Found", "2": "Medical Emergency", "3": "Information Center"}

        if choice in issue_map:
            name = input("Enter your name: ")
            description = input("Describe your issue: ")

            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO public_helpline_logs (name, issue_type, description, logged_time)
                VALUES (%s, %s, %s, %s)
            """, (name, issue_map[choice], description, datetime.now()))
            connection.commit()

            print("✅ Your issue has been logged. Help will arrive shortly.")
            cursor.close()
            connection.close()
        else:
            print("❌ Invalid option.")
