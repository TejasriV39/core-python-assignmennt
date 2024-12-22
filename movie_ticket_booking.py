def book_seat(booked_seats, seat):
    if seat in booked_seats:
        return "Seat already booked."
    booked_seats.append(seat)
    return booked_seats

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
    else:
        return "Seat not booked."
    return booked_seats

def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

# User input
total_seats = int(input("Enter total number of seats: "))
booked_seats = list(map(int, input("Enter booked seats separated by spaces: ").split()))
book_seat_input = int(input("Enter seat number to book: "))
cancel_seat_input = int(input("Enter seat number to cancel: "))

booked_seats = book_seat(booked_seats, book_seat_input)
booked_seats = cancel_seat(booked_seats, cancel_seat_input)
available = available_seats(total_seats, booked_seats)

print(f"Available seats: {available}")