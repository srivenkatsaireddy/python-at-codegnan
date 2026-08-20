from tracker import CareerTracker
def main():
    tracker = CareerTracker()
    while True:
        print("      CAREER APPLICATION TRACKER")
        print(" ")

        print("1. Add Application")
        print("2. View Applications")
        print("3. Search Application")
        print("4. Update Status")
        print("5. Delete Application")
        print("6. Exit")

        choice = int(input("\nEnter your choice : "))

        if choice == 1:
            tracker.add_application()

        elif choice == 2:
            tracker.view_applications()

        elif choice == 3:
            tracker.search_application()

        elif choice == 4:
            tracker.update_status()

        elif choice == 5:
            tracker.delete_application()

        elif choice == 6:
            print("\nThank You for using Career Application Tracker.")
            break

        else:
            print("\nInvalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()