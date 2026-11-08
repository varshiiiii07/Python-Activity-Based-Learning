
def assign_seats(seating_rows, attendees):
    assignments = {}
    index = 0

    for row_number, row in enumerate(
        seating_rows, start=1
    ):
        for seat in row:
            if index < len(attendees):
                assignments[attendees[index]] = (
                    f"Row {row_number}, Seat {seat}"
                )
                index += 1

    return assignments


def validate_entries(registered_ids, ticket_ids):
    registered = set(registered_ids)
    seen = set()
    valid = []
    invalid = []
    duplicates = []

    for ticket in ticket_ids:
        if ticket not in registered:
            invalid.append(ticket)
        elif ticket in seen:
            duplicates.append(ticket)
        else:
            valid.append(ticket)
            seen.add(ticket)

    return valid, invalid, duplicates


def main():
    seating_rows = [
        ["A1", "A2", "A3", "A4"],
        ["B1", "B2", "B3", "B4"],
        ["C1", "C2", "C3", "C4"]
    ]

    registered_ids = [
        "REG101", "REG102", "REG103",
        "REG104", "REG105"
    ]

    ticket_ids = [
        "REG101", "REG102", "REG101",
        "REG999", "REG104"
    ]

    assignments = assign_seats(
        seating_rows, registered_ids
    )

    valid, invalid, duplicates = validate_entries(
        registered_ids, ticket_ids
    )

    total_seats = sum(
        len(row) for row in seating_rows
    )
    assigned_seats = len(assignments)

    print("CAMPUS EVENT SEATING AND ENTRY VALIDATION")

    print("\\nSEATING ASSIGNMENTS")
    for attendee, seat in assignments.items():
        print(f"{attendee}: {seat}")

    print("\\nENTRY VALIDATION")
    print("Valid entries:", valid)
    print("Invalid tickets:", invalid)
    print("Duplicate entries:", duplicates)

    print("\\nSEATING CAPACITY")
    print("Total seats:", total_seats)
    print("Assigned seats:", assigned_seats)
    print("Available seats:",
          total_seats - assigned_seats)


if __name__ == "__main__":
    main()

