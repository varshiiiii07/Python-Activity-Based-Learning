


buildings = {
    "Academic Block": {
        "electricity": [120, 135, 150],
        "water": [18, 20, 24]
    },
    "Library": {
        "electricity": [80, 78, 90],
        "water": [12, 11, 13]
    },
    "Hostel": {
        "electricity": [200, 220, 250],
        "water": [35, 40, 45]
    }
}

# Rates and daily consumption thresholds
electricity_rate = 8
water_rate = 30
electricity_limit = 140
water_limit = 25

results = []

for name, data in buildings.items():
    electricity = data["electricity"]
    water = data["water"]

    total_e = sum(electricity)
    total_w = sum(water)

    avg_e = total_e / len(electricity)
    avg_w = total_w / len(water)

    cost_e = total_e * electricity_rate
    cost_w = total_w * water_rate
    total_cost = cost_e + cost_w

    print("\n---", name, "---")
    print("Total electricity:", total_e, "kWh")
    print("Total water:", total_w, "kL")
    print("Average electricity:", round(avg_e, 2))
    print("Average water:", round(avg_w, 2))
    print("Electricity cost: Rs.", cost_e)
    print("Water cost: Rs.", cost_w)
    print("Total cost: Rs.", total_cost)

    # Calculate daily percentage changes
    for label, readings in [
        ("Electricity", electricity),
        ("Water", water)
    ]:
        print(label, "percentage changes:")

        for i in range(1, len(readings)):
            previous = readings[i - 1]
            current = readings[i]

            if previous == 0:
                print("Day", i, "to", i + 1,
                      ": Undefined")
            else:
                change = (
                    (current - previous) / previous
                ) * 100

                print(
                    "Day", i, "to", i + 1,
                    ":", round(change, 2), "%"
                )

    # Identify excessive consumption
    alerts = []

    if avg_e > electricity_limit:
        alerts.append("Excessive electricity")

    if avg_w > water_limit:
        alerts.append("Excessive water")

    if not alerts:
        alerts.append("Within thresholds")

    # Calculate weighted performance score
    score = (
        50 * avg_e / electricity_limit
        + 50 * avg_w / water_limit
    )

    results.append({
        "name": name,
        "cost": total_cost,
        "score": score,
        "alerts": alerts
    })

# Rank buildings by score
results.sort(key=lambda item: item["score"])

print("\n===== CAMPUS AUDIT SUMMARY =====")
print("Rank | Building | Total Cost | Score | Status")

for rank, item in enumerate(results, start=1):
    print(
        rank, "|",
        item["name"], "|",
        "Rs.", round(item["cost"], 2), "|",
        round(item["score"], 2), "|",
        ", ".join(item["alerts"])
    )

print("\nAudit completed.")
