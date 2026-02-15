from database import session,Movie,Showtime,Seat

def setup_data():
    movie1 = Movie(title = "Inception")
    session.add(movie1)
    session.commit()

    show1 = Showtime(movie_id = movie1.id , time = "10:00 AM")
    session.add(show1)
    session.commit()

    rows = ['A' , 'B' , 'C' , 'D' , 'E']
    cols = range(1,6)

    for row in rows:
        for col in cols:
            seat = Seat(showtime_id = show1.id , seat_no = f"{row}{col}")
            session.add(seat)

        session.commit()
    
setup_data()
        
