import tkinter as tk
from tkinter import messagebox, font
from database import session, Movie, Showtime, Seat, Booking

class BookingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🎬 Movie Ticket Booking System")
        self.master.geometry("700x650")
        self.master.configure(bg="#f0f2f5")

        self.selected_movie = None
        self.selected_showtime = None
        self.selected_seats = set()

        self.build_main_screen()

    def build_main_screen(self):
        title_font = ("Arial", 18, "bold")
        label_font = ("Arial", 12)
        btn_font = ("Arial", 10, "bold")

        tk.Label(self.master, text="🎟️ Movie Ticket Booking", font=title_font, bg="#f0f2f5").pack(pady=20)

        # Movie dropdown
        tk.Label(self.master, text="Select Movie", font=label_font, bg="#f0f2f5").pack()
        self.movie_var = tk.StringVar()
        self.movie_var.set("Select a Movie")
        self.movie_dropdown = tk.OptionMenu(self.master, self.movie_var, "Select a Movie", command=self.update_showtimes)
        self.movie_dropdown.config(font=label_font, width=25)
        self.movie_dropdown.pack(pady=5)

        # Showtime dropdown
        tk.Label(self.master, text="Select Showtime", font=label_font, bg="#f0f2f5").pack()
        self.showtime_var = tk.StringVar()
        self.showtime_var.set("Select Showtime")
        self.showtime_dropdown = tk.OptionMenu(self.master, self.showtime_var, "Select Showtime", command=self.show_seats)
        self.showtime_dropdown.config(font=label_font, width=25)
        self.showtime_dropdown.pack(pady=5)

        # Seat frame
        self.frame_seats = tk.Frame(self.master, bg="#f0f2f5")
        self.frame_seats.pack(pady=20)

        # User name
        self.entry_name = tk.Entry(self.master, font=label_font, width=40)
        self.entry_name.insert(0, "Enter your name")
        self.entry_name.pack(pady=10)

        # Book button
        self.book_btn = tk.Button(self.master, text="Book Selected Seats", font=btn_font, bg="#007bff", fg="white",
                                  activebackground="#0056b3", command=self.book)
        self.book_btn.pack(pady=15)

        self.load_movies()

    def load_movies(self):
        self.movies = session.query(Movie).all()
        menu = self.movie_dropdown["menu"]
        menu.delete(0, "end")
        for m in self.movies:
            menu.add_command(label=m.title, command=lambda value=m.title: self.movie_var.set(value))

    def update_showtimes(self, selected_title):
        movie = next((m for m in self.movies if m.title == selected_title), None)
        self.selected_movie = movie
        self.showtimes = session.query(Showtime).filter_by(movie_id=movie.id).all()

        menu = self.showtime_dropdown["menu"]
        menu.delete(0, "end")
        for st in self.showtimes:
            label = f"{st.id} - {st.time}"
            menu.add_command(label=label, command=lambda value=label: self.showtime_var.set(value))

    def show_seats(self, selected_show_label):
        self.selected_showtime = int(selected_show_label.split(' - ')[0])
        seats = session.query(Seat).filter_by(showtime_id=self.selected_showtime).all()

        for widget in self.frame_seats.winfo_children():
            widget.destroy()

        self.seat_buttons = {}
        rows = ["A", "B", "C", "D", "E"]
        cols = range(1, 6)

        for r_idx, row in enumerate(rows):
            for c in cols:
                seat_number = f"{row}{c}"
                seat = next((s for s in seats if s.seat_number == seat_number), None)
                if seat:
                    color = "green" if seat.is_booked == 0 else "red"
                    state = "normal" if seat.is_booked == 0 else "disabled"
                    btn = tk.Button(self.frame_seats, text=seat_number, width=5, height=2,
                                    bg=color, fg="white", state=state,
                                    font=("Arial", 10, "bold"))
                    btn.grid(row=r_idx, column=c, padx=5, pady=5)
                    btn.config(command=lambda sn=seat_number, b=btn: self.toggle_seat(sn, b))
                    self.seat_buttons[seat_number] = btn

    def toggle_seat(self, seat_number, button):
        if seat_number in self.selected_seats:
            self.selected_seats.remove(seat_number)
            button.config(bg="green")
        else:
            self.selected_seats.add(seat_number)
            button.config(bg="orange")

    def book(self):
        name = self.entry_name.get().strip()
        if not name or not self.selected_seats:
            messagebox.showerror("Error", "Please enter your name and select at least one seat.")
            return

        for seat_number in self.selected_seats:
            seat = session.query(Seat).filter_by(showtime_id=self.selected_showtime, seat_number=seat_number).first()
            if seat.is_booked:
                messagebox.showerror("Error", f"Seat {seat_number} is already booked.")
                return

        for seat_number in self.selected_seats:
            seat = session.query(Seat).filter_by(showtime_id=self.selected_showtime, seat_number=seat_number).first()
            seat.is_booked = 1

        booking = Booking(user_name=name, showtime_id=self.selected_showtime,
                          seat_numbers=",".join(self.selected_seats))
        session.add(booking)
        session.commit()

        messagebox.showinfo("Success", f"Booking Confirmed!\nSeats: {', '.join(self.selected_seats)}")
        self.selected_seats.clear()
        self.show_seats(self.showtime_var.get())

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()
