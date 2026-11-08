

accounts = {
    "A101": 1000.0,
    "A102": 500.0
}

transactions = [
    ("DEPOSIT", "A101", 200),
    ("WITHDRAW", "A101", 100),
    ("TRANSFER", "A101", "A102", 150),
    ("WITHDRAW", "A101", 100),
    ("WITHDRAW", "A101", 100),
    ("WITHDRAW", "A101", 5000),
    ("DEPOSIT", "A102", -50)
]

history = []
pattern_count = {}
suspicious = []

for txn in transactions:
    action = txn[0]
    valid = False
    pattern = None

    if action == "DEPOSIT":
        _, account, amount = txn
        pattern = (action, account, amount)

        if account in accounts and amount > 0:
            accounts[account] += amount
            valid = True

    elif action == "WITHDRAW":
        _, account, amount = txn
        pattern = (action, account, amount)

        if account not in accounts or amount <= 0:
            pass
        elif accounts[account] >= amount:
            accounts[account] -= amount
            valid = True

    elif action == "TRANSFER":
        _, source, target, amount = txn
        pattern = (action, source, target, amount)

        if (source in accounts and target in accounts
                and source != target and amount > 0
                and accounts[source] >= amount):
            accounts[source] -= amount
            accounts[target] += amount
            valid = True

    else:
        print("Unknown transaction type:", action)

    if pattern is not None:
        pattern_count[pattern] = (
            pattern_count.get(pattern, 0) + 1
        )

        if pattern_count[pattern] == 3:
            suspicious.append(pattern)

    history.append((txn, "Valid" if valid else "Invalid"))

    print(txn, "->", "Accepted" if valid else "Rejected")

print("\n--- TRANSACTION AUDIT REPORT ---")

for txn, status in history:
    print(txn, ":", status)

print("\n--- FINAL ACCOUNT BALANCES ---")
for account, balance in accounts.items():
    print(account, ":", round(balance, 2))

print("\n--- SUSPICIOUS PATTERN REPORT ---")
if suspicious:
    for pattern in suspicious:
        print("Repeated pattern (3 or more attempts):", pattern)
else:
    print("No repeated patterns detected.")
