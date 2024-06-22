items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]["cost"] for item in item_names]
    calories = [items[item]["calories"] for item in item_names]

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    selected_items = []

    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]
            total_cost += costs[i - 1]

    selected_items.reverse()
    return selected_items, total_cost, total_calories


budget = 100

selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(
    items, budget
)
print(f"Selected items (Greedy): {selected_items_greedy}")
print(f"Total cost: {total_cost_greedy}")
print(f"Total calories: {total_calories_greedy}")

selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
print(f"Selected items (DP): {selected_items_dp}")
print(f"Total cost: {total_cost_dp}")
print(f"Total calories: {total_calories_dp}")
