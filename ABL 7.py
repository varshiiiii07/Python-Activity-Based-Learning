

key = [
    x.strip().upper()
    for x in input(
        "Enter answer key separated by commas: "
    ).split(",")
]

if not key or any(x == "" for x in key):
    print("Invalid answer key.")
else:
    students = int(input("Enter number of students: "))

    if students <= 0:
        print("Number of students must be positive.")
    else:
        correct = [0] * len(key)
        total = [0] * len(key)

        for i in range(students):
            while True:
                answers = [
                    x.strip().upper()
                    for x in input(
                        f"Student {i + 1} answers: "
                    ).split(",")
                ]

                if len(answers) == len(key):
                    break

                print("Enter exactly", len(key), "answers.")

            for j in range(len(key)):
                total[j] += 1
                if answers[j] == key[j]:
                    correct[j] += 1

        rates = []

        print("\n--- QUESTION-WISE ANALYSIS ---")

        for j in range(len(key)):
            rate = correct[j] / total[j] * 100
            missed = total[j] - correct[j]
            rates.append(rate)

            if rate >= 80:
                category = "Excellent"
            elif rate >= 60:
                category = "Good"
            elif rate >= 40:
                category = "Average"
            else:
                category = "Poor"

            print(f"\nQuestion {j + 1}")
            print("Correct:", correct[j])
            print("Incorrect:", missed)
            print("Success rate:", round(rate, 2), "%")
            print("Classification:", category)

        most_missed = max(
            total[j] - correct[j]
            for j in range(len(key))
        )

        print("\n--- MOST FREQUENTLY MISSED ---")
        for j in range(len(key)):
            missed = total[j] - correct[j]
            if missed == most_missed:
                print(f"Question {j + 1}: {missed} missed")

        print("\nAnalysis completed.")
