def knapsack_frac(num_items, box, max_weight, index):
    if index == num_items or max_weight <= 0:
        return 0

    if box[index]["weight"] <= max_weight:
        profitin = box[index]["profit"] + knapsack_frac(
            len(box), box, max_weight - box[index]["weight"], index + 1
        )
        profitout = knapsack_frac(len(box), box, max_weight, index + 1)
    else:
        profitin = box[index]["profit"] * (max_weight / box[index]["weight"])
        profitout = knapsack_frac(len(box), box, max_weight, index + 1)
    return max(profitin, profitout)


# Test case
box = [
    {"weight": 10, "profit": 60},
    {"weight": 20, "profit": 100},
    {"weight": 30, "profit": 120},
]
max_weight = 50
expected_output = 240.0
assert knapsack_frac(len(box), box, max_weight, 0) == expected_output
