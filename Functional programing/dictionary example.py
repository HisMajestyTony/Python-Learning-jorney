transactions = [
    ("2026-01", "income", 2000),
    ("2026-01", "expense", 500),
    ("2026-02", "income", 2200),
    ("2026-02", "expense", 700),
]

summary = {}

for month, type_, amount in transactions:

    if month not in summary:
        summary[month] = {"income":0, "expense":0}

    summary[month][type_] += amount

print(summary)