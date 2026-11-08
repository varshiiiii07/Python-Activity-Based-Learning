

data = []
locations = int(input("Enter number of locations: "))

lower = float(input("Enter lower threshold: "))
upper = float(input("Enter upper threshold: "))

if locations <= 0 or lower > upper:
    print("Invalid number of locations or thresholds.")

else:
    for i in range(locations):
        name = input("\nEnter location name: ")
        values = input(
            "Enter readings separated by commas: "
        )
        readings = [float(x.strip())
                    for x in values.split(",")]

        if not readings:
            print("No readings entered.")
            continue

        data.append([name, readings])

    total = []
    counts = {"Low": 0, "Normal": 0, "High": 0}

    for name, readings in data:
        avg = sum(readings) / len(readings)
        maximum = max(readings)
        minimum = min(readings)

        print("\nLocation:", name)
        print("Readings:", readings)
        print("Average:", round(avg, 2))
        print("Maximum:", maximum)
        print("Minimum:", minimum)

        for value in readings:
            if value < lower:
                category = "Low"
            elif value <= upper:
                category = "Normal"
            else:
                category = "High"

            counts[category] += 1
            print(value, "->", category)

        total.extend(readings)

    if total:
        print("\n--- Overall Summary ---")
        print("Total readings:", len(total))
        print("Overall average:",
              round(sum(total) / len(total), 2))
        print("Overall maximum:", max(total))
        print("Overall minimum:", min(total))
        print("Low readings:", counts["Low"])
        print("Normal readings:", counts["Normal"])
        print("High readings:", counts["High"])
