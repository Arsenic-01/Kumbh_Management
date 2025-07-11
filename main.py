from ticket_module import TicketReservation
from lodging_module import LodgingReservation
from helpline_module import PublicHelpline
from police_module import PoliceHelpline

def main():
    ticket_sys = TicketReservation()
    lodge_sys = LodgingReservation()
    pub_help = PublicHelpline()
    police_help = PoliceHelpline()

    while True:
        print("\n====== Kumbh Mela Management System ======")
        print("1. Ticket Reservation")
        print("2. Lodging Reservation")
        print("3. Public Helpline")
        print("4. Police Helpline")
        print("5. View Ticket")
        print("6. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            ticket_sys.book_ticket()
        elif choice == "2":
            lodge_sys.reserve_lodge()
        elif choice == "3":
            pub_help.show_menu()
        elif choice == "4":
            police_help.report_incident()
        elif choice == "5":
            ticket_sys.view_ticket()
        elif choice == "6":
            print("Thank you. Exiting...")
            break


if __name__ == "__main__":
    main()