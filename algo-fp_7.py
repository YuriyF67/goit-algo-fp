import random

# Кількість імітацій кидання кубиків
num_simulations = 1000000

# Словник для зберігання кількості випадків кожної суми
sum_counts = {i: 0 for i in range(2, 13)}

# Імітація кидання кубиків
for _ in range(num_simulations):
    # Кидання двох кубиків
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Обчислення суми
    sum_value = die1 + die2

    # Збільшення лічильника для відповідної суми
    sum_counts[sum_value] += 1

# Обчислення ймовірностей
probabilities = {
    sum_value: count / num_simulations for sum_value, count in sum_counts.items()
}

# Виведення результатів
print("Ймовірності сум при киданні двох кубиків (метод Монте-Карло):")
for sum_value, probability in sorted(probabilities.items()):
    print(f"Сума {sum_value}: {probability:.6f}")

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

print("\nАналітичні ймовірності:")
for sum_value, probability in sorted(analytical_probabilities.items()):
    print(f"Сума {sum_value}: {probability:.6f}")
