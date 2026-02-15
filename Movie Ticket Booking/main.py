from database import session , Movie , Seat , Showtime , Booking, User

def register():
    print("Register New User")
    username = input("Enter UserName: ").strip()
    existing = session.query(User).filter_by(username = username).first()
    if existing:
        print("Username Already Exists")
        return 
    password = input("Enter Password: ").strip()
    user = User(username = username, password = password)
    session.add(user)
    session.commit()
    print("")


def list_movies_and_showtimes():
    movies = session.query(Movie).all()
    for movie in movies:
        print(f"    Movie:  {movie.id}. {movie.title}")
        for showtime in movie.showtimes:
            print(f"       Showtime:  {showtime.id} --> {showtime.time}")


def display_seats(showtime_id):
    seats = session.query(Seat).filter_by(showtime_id=showtime_id).all()
    print(f"\n Seat Map for Showtime {showtime_id}:")
    row = ""
    for i, seat in enumerate(seats, start=1):
        status = 'X' if seat.is_booked else seat.seat_no
        row += f"{status} "
        if i % 5 == 0:
            print(row)
            row = ""
    if row: print(row)


def book_seats(user_name, showtime_id, seat_numbers):
    seats_to_book = session.query(Seat).filter(
        Seat.showtime_id == showtime_id,
        Seat.seat_no.in_(seat_numbers),
        Seat.is_booked == 0
    ).all()

    if len(seats_to_book) != len(seat_numbers):
        print("❌ Some seats are already booked or invalid....Choose Another Seat")
        return

    # Mark seats as booked
    for seat in seats_to_book:
        seat.is_booked = 1

    # Save booking
    booking = Booking(
        user_name=user_name,
        showtime_id=showtime_id,
        seat_number=",".join(seat_numbers)
    )
    session.add(booking)
    session.commit()

    print(f"✅ Booking confirmed for {user_name}..... Seats: {', '.join(seat_numbers)}")


def main():
    while True:
        print("\n ------------------------------\n |                            | ")
        print(" | 1. View Movies & Showtimes |\n | 2. Book Tickets            |\n | 3. Exit                    |")
        print(" |                            | \n ------------------------------")
        choice = input("Enter choice: ")

        if choice == '1':
            list_movies_and_showtimes()

        elif choice == '2':
            list_movies_and_showtimes()

            showtime_id = int(input("Enter showtime ID: "))
            display_seats(showtime_id)
            seat_input = input("Enter seat numbers to book (comma-separated): ")
            seat_numbers = [s.strip().upper() for s in seat_input.split(',')]
            user_name = input("Enter your name: ")
            book_seats(user_name, showtime_id, seat_numbers)

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

                

