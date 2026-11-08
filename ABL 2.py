
def is_eligible(marks, assessment, attendance):
    return (
        marks >= 60
        and assessment >= 50
        and attendance >= 75
    )


def calculate_score(marks, assessment, attendance):
    return (
        0.5 * marks
        + 0.3 * assessment
        + 0.2 * attendance
    )


def rank_key(candidate):
    return (
        -candidate["score"],
        -candidate["marks"],
        -candidate["assessment"],
        -candidate["attendance"],
        candidate["name"].lower()
    )


def main():
    candidates = [
        {
            "name": "Alice",
            "marks": 85,
            "assessment": 90,
            "attendance": 95
        },
        {
            "name": "Bob",
            "marks": 75,
            "assessment": 80,
            "attendance": 78
        },
        {
            "name": "Charlie",
            "marks": 60,
            "assessment": 50,
            "attendance": 80
        },
        {
            "name": "David",
            "marks": 58,
            "assessment": 70,
            "attendance": 85
        },
        {
            "name": "Eva",
            "marks": 90,
            "assessment": 95,
            "attendance": 90
        }
    ]

    qualified = []
    ineligible = []

    for candidate in candidates:
        if is_eligible(
            candidate["marks"],
            candidate["assessment"],
            candidate["attendance"]
        ):
            candidate["score"] = calculate_score(
                candidate["marks"],
                candidate["assessment"],
                candidate["attendance"]
            )
            qualified.append(candidate)
        else:
            ineligible.append(candidate)

    qualified.sort(key=rank_key)

    print("RANKED QUALIFIED CANDIDATES")
    for rank, candidate in enumerate(qualified, start=1):
        print(
            rank,
            candidate["name"],
            "- Score:",
            round(candidate["score"], 2)
        )

    print("\\nINELIGIBLE CANDIDATES")
    for candidate in ineligible:
        print(candidate["name"])


if __name__ == "__main__":
    main()
