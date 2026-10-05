# CSE325-2026-L02-M4RB
QUALITY_BASELINE = "pre-refactor"

def process_orders(raw_orders):
    d = {}
    for line in raw_orders:
        parts = line.split(",")
        name = parts[0]
        qty = int(parts[1])
        price = float(parts[2])
        total = qty * price
        if total > 500:
            total = total * 0.9
        elif total > 200:
            total = total * 0.95
        d[name] = d.get(name, 0) + total

    for name in d:
        if d[name] > 500:
            d[name] = d[name]
        elif d[name] > 200:
            d[name] = d[name]

    print("ORDER REPORT")
    print("------------")
    for name in d:
        val = d[name]
        if val > 500:
            tier = "GOLD"
        elif val > 200:
            tier = "SILVER"
        else:
            tier = "STANDARD"
        print(f"{name}: ${val:.2f} ({tier})")

    total_all = 0
    for name in d:
        total_all = total_all + d[name]
    print(f"TOTAL: ${total_all:.2f}")
    return d


if __name__ == "__main__":
    sample = [
        "Alice,3,150.00",
        "Bob,10,60.00",
        "Alice,1,300.00",
        "Carol,2,45.00",
    ]
    process_orders(sample)