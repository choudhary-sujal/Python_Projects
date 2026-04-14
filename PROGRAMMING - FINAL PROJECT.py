print("PVR CINEMAS")

# The class venue represents the name, seting map of the system
class Venue:
    def __init__(self, name, rows, columns, prices):
        self.name = name  # Name of the System
        self.rows = rows  # Number of rows
        self.columns = columns  # Number of columns 
        # Create a list representing seats ("A" for Available, "NA" for Not Available)
        self.seats = [["A" for _ in range(columns)] for _ in range(rows)]
        self.prices = prices  # list for ticket prices corresponding to each seat

    def display_seating(self):
        # Display the current seating map with column and row 
        print(f"\n{self.name} - Seating Map (A: Available, NA: Not Available):")
        print("   " + " ".join([f"C{col}" for col in range(self.columns)]))  # Column headers
        for i, row in enumerate(self.seats):
            print(f"R{i} " + " ".join(row))  # Row headers

    def book_seat(self, row, col):
        # Check if the seat is within range and available
        if 0 <= row < self.rows and 0 <= col < self.columns and self.seats[row][col] == "A":
            self.seats[row][col] = "NA"  # Mark the seat as booked
            return self.prices[row][col]  # Return the price of the booked seat
        return None  # Return None if the seat cannot be booked

# The class represents the user registraion and interaction
class TicketReservationSystem:
    def __init__(self, venue):
        self.venue = venue  # The venue object having seat and price
        self.selected_seats = []  # List of selected seats for booking
        self.total_cost = 0.0  # Total cost of selected seats
        self.registered_users = {}  # Dictionary to store user details (username: (password, email))
        self.current_user = None  # To keep track of the logged-in user

    def register_user(self):
        # Register a new user with username, email, and password, basically for a new user
        username = input("Enter a username: ")
        if username in self.registered_users:
            print("Username already exists. Please choose another.")
            return
        email = input("Enter your Gmail address: ")
        if "@gmail.com" not in email:
            print("Please enter a valid Gmail address.")
            return
        password = input("Enter a password: ")
        self.registered_users[username] = (password, email)
        print("Registration successful! Please log in to proceed.")

    def login_user(self):
        # Log in an existing user with username and password
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_data = self.registered_users.get(username)
        if user_data and user_data[0] == password:
            self.current_user = username
            print(f"Welcome back, {username}! You are now logged in.")
        else:
            print("Invalid username or password. Please try again.")

    def reserve_seat(self):
        # Reserve a seat for the logged-in user
        if not self.current_user:
            print("Please log in to reserve a seat.")
            return
        try:
            row = int(input("Enter Row (0-indexed): "))
            col = int(input("Enter Column (0-indexed): "))
            price = self.venue.book_seat(row, col)  # Attempt to book the seat
            if price is not None:
                self.selected_seats.append((row, col, price))
                self.total_cost += price
                print(f"Congrats! Your Seat (R{row}, C{col}) is booked successfully! Please Pay: ${price:.2f}")
            else:
                print("Sorry! The seat is already booked or invalid.")
        except ValueError:
            print("Error: Please enter valid numbers for row and column.")

    def confirm_reservation(self):
        # Confirm and finalize the reservation for the user
        if not self.current_user:
            print("Please log in to confirm a reservation.")
            return
        if not self.selected_seats:
            print("No seats selected! Please reserve your seats first to confirm your reservation.")
            return

        print("\n-- Booking Confirmation --")
        for row, col, price in self.selected_seats:
            print(f"Seat (R{row}, C{col}): ${price:.2f}")
        print(f"Total Cost: ${self.total_cost:.2f}")
        print(f"Reservation Confirmed! Thank you for choosing PVR CINEMA, {self.current_user}.")

        # Reset the details for user for new booking
        self.selected_seats = []
        self.total_cost = 0.0

    def run(self):
        # Main loop for the ticket reservation system
        while True:
            print("\nWelcome to PVR CINEMA TICKET COUNTER. Please choose an option:")
            print("1. New User! Register")
            print("2. Log in")
            print("3. Display Seating Map")
            print("4. Reserve a Seat")
            print("5. Confirm Reservation")
            print("6. Exit")

            choice = input("Enter your choice from the above mentioned details: ")
            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login_user()
            elif choice == '3':
                self.venue.display_seating()
            elif choice == '4':
                self.reserve_seat()
            elif choice == '5':
                self.confirm_reservation()
            elif choice == '6':
                print("Thank you for using the PVR CINEMA Ticket Reservation System!")
                break
            else:
                print("Invalid choice. Please try again.")

# Main execution block
if __name__ == "__main__":
    # Initialize the venue with name, seating arrangements and prices
    venue_name = "PVR CINEMA"
    rows, columns = 3, 5
    prices = [
        [50, 60, 50, 60, 50],
        [60, 70, 60, 70, 70],
        [50, 60, 50, 50, 60]
    ]
    venue = Venue(venue_name, rows, columns, prices)  # Create the venue object
    system = TicketReservationSystem(venue)  # Create the reservation system object
    system.run()  # Run the system
