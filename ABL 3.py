

locations = int(input("Enter number of locations: "))

total_received = 0
total_distributed = 0
total_damaged = 0
total_replenishment = 0

for i in range(1, locations + 1):
    print("\nLocation", i)

    name = input("Enter location name: ")
    opening = float(input("Enter opening stock (kg): "))
    received = float(input("Enter received stock (kg): "))
    distributed = float(input("Enter distributed stock (kg): "))
    damaged = float(input("Enter damaged stock (kg): "))
    actual = float(input("Enter actual closing stock (kg): "))
    minimum = float(input("Enter minimum stock level (kg): "))

    if min(opening, received, distributed,
           damaged, actual, minimum) < 0:
        print("Invalid input: quantities cannot be negative.")
        print("Please run the program again.")
        break

    available = opening + received
    expected = available - distributed - damaged

    discrepancy = actual - expected
    replenishment = max(0, minimum - actual)

    print("\n--- Stock Reconciliation Report ---")
    print("Location:", name)
    print("Total available stock:", available, "kg")
    print("Expected closing stock:", expected, "kg")
    print("Actual closing stock:", actual, "kg")
    print("Discrepancy:", discrepancy, "kg")

    if discrepancy == 0:
        print("Status: Stock reconciled")
    elif discrepancy < 0:
        print("Status: Stock shortage")
    else:
        print("Status: Excess stock")

    print("Replenishment required:", replenishment, "kg")

    total_received += received
    total_distributed += distributed
    total_damaged += damaged
    total_replenishment += replenishment

else:
    print("\n--- Overall Summary ---")
    print("Total received:", total_received, "kg")
    print("Total distributed:", total_distributed, "kg")
    print("Total damaged:", total_damaged, "kg")
    print("Total replenishment required:",
          total_replenishment, "kg")
