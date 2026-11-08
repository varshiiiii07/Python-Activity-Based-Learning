

branches = {
    "Branch A": {"Rice": 80, "Oil": 20},
    "Branch B": {"Rice": 25, "Oil": 60},
    "Branch C": {"Rice": 45, "Oil": 30}
}

targets = {
    "Rice": 50,
    "Oil": 40
}

max_transfer = 15
transfers = []

# Process each product
for product, target in targets.items():

    surplus = {}
    shortage = {}

    # Calculate surplus and shortage
    for branch, stock in branches.items():
        quantity = stock.get(product, 0)

        if quantity > target:
            surplus[branch] = quantity - target
        elif quantity < target:
            shortage[branch] = target - quantity

    # Transfer stock between branches
    for donor in list(surplus.keys()):
        for receiver in list(shortage.keys()):

            if surplus[donor] <= 0:
                break

            if shortage[receiver] <= 0:
                continue

            quantity = min(
                surplus[donor],
                shortage[receiver],
                max_transfer
            )

            if quantity > 0:
                # Update inventory
                branches[donor][product] -= quantity
                branches[receiver][product] += quantity

                # Record transfer as a tuple
                transfers.append(
                    (product, donor, receiver, quantity)
                )

                surplus[donor] -= quantity
                shortage[receiver] -= quantity

print("\n--- INVENTORY TRANSFERS ---")

if transfers:
    for product, donor, receiver, quantity in transfers:
        print(
            product, ":", donor, "->", receiver,
            "| Quantity:", quantity
        )
else:
    print("No transfers required.")

# Display final inventory
print("\n--- FINAL BRANCH INVENTORY ---")

for branch, stock in branches.items():
    print(branch, ":", stock)

# Display remaining surplus and shortage
print("\n--- FINAL STOCK STATUS ---")

for branch, stock in branches.items():
    for product, target in targets.items():
        quantity = stock.get(product, 0)

        if quantity < target:
            print(
                branch, product,
                "Shortage:", target - quantity
            )
        elif quantity > target:
            print(
                branch, product,
                "Surplus:", quantity - target
            )
        else:
            print(branch, product, "Stock at target")

print("\nInventory transfer analysis completed.")
