

# Student groups: (group_id, student_ids, category)
groups = [
    ("G1", ["S101", "S102"], "UG"),
    ("G2", ["S103", "S104", "S105"], "UG"),
    ("G3", ["S106", "S107"], "PG"),
    ("G4", ["S108", "S109", "S110"], "PG"),
    ("G5", ["S102", "S111"], "UG")
]

# Room details: capacity and eligible categories
rooms = {
    "Room A": {"capacity": 3, "eligible": ["UG"]},
    "Room B": {"capacity": 2, "eligible": ["PG"]},
    "Room C": {"capacity": 4, "eligible": ["UG", "PG"]}
}

# Initialize allocation records
occupancy = {room: [] for room in rooms}
allocations = []
seen_students = set()
assigned_students = set()
duplicate_ids = set()

# Allocate each group
for group_id, students, category in groups:

    # Detect duplicate student IDs across groups
    duplicates = [
        student for student in students
        if student in seen_students
    ]

    if duplicates:
        duplicate_ids.update(duplicates)
        print("Duplicate assignment detected:",
              group_id, duplicates)
        continue

    seen_students.update(students)
    allocated = False

    # Find a room satisfying eligibility and capacity
    for room, details in rooms.items():
        available = (
            details["capacity"] - len(occupancy[room])
        )

        if (category in details["eligible"]
                and len(students) <= available):

            occupancy[room].extend(students)
            assigned_students.update(students)

            allocations.append(
                (group_id, room, students)
            )

            print(group_id, "allocated to", room)
            allocated = True
            break

    if not allocated:
        print(group_id, "could not be allocated")

# Display final room allocations
print("\n--- FINAL ROOM ALLOCATION ---")

for room, students in occupancy.items():
    print(room, ":", students)
    print("Occupied:", len(students),
          "/", rooms[room]["capacity"])

# Display duplicate IDs
print("\n--- DUPLICATE ASSIGNMENTS ---")

if duplicate_ids:
    for student in sorted(duplicate_ids):
        print("Duplicate student ID:", student)
else:
    print("No duplicates detected.")

# Calculate unallocated demand using unique student IDs
all_students = {
    student
    for group_id, students, category in groups
    for student in students
}

unallocated = all_students - assigned_students

print("\n--- UNALLOCATED STUDENTS ---")
print(sorted(unallocated))
print("Unallocated demand:", len(unallocated))
print("Allocated students:", len(assigned_students))
print("Total unique students:", len(all_students))

print("\nHostel allocation analysis completed.")
