warehouse = {
    "Гипсокартон": {"quantity": 120, "price": 415.00, "min_quantity": 70},
    "Шпаклёвка": {"quantity": 84, "price": 370.00, "min_quantity": 40},
    "Грунтовка": {"quantity": 18, "price": 295.00, "min_quantity": 24},
    "Краска": {"quantity": 33, "price": 760.00, "min_quantity": 20},
    "Плитка": {"quantity": 12, "price": 1390.00, "min_quantity": 16},
}

# Выводим таблицу с основными данными по складу
print("=" * 70)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 70)
print()
print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 70)

# Эти переменные нужны для накопления общей статистики
total_cost = 0
critical_items = []
most_expensive_material = ""
most_expensive_cost = 0

for material_name, material_data in warehouse.items():
    # Получаем остаток, цену и минимальный допустимый запас
    quantity_value = material_data["quantity"]
    price_value = material_data["price"]
    min_quantity_value = material_data["min_quantity"]
    item_total_cost = quantity_value * price_value

    total_cost += item_total_cost

    # Запоминаем материал с максимальной суммарной стоимостью
    if item_total_cost > most_expensive_cost:
        most_expensive_cost = item_total_cost
        most_expensive_material = material_name

    status_flag = ""
    # Если остаток меньше минимального, помечаем позицию как критическую
    if quantity_value < min_quantity_value:
        status_flag = "  CRITICAL"
        critical_items.append(
            f"{material_name}: {quantity_value} < {min_quantity_value}"
        )

    print(
        f"{material_name} | {quantity_value} | {price_value:.2f} | "
        f"{min_quantity_value} | {item_total_cost:.2f}{status_flag}"
    )

print("=" * 70)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")
print(
    f"Самый дорогой: {most_expensive_material} "
    f"({most_expensive_cost:.2f} руб)"
)
print()
print(f"КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")

if critical_items:
    for material_name in critical_items:
        print(f"- {material_name}")
else:
    print("Нет критических остатков")

print()
print("=== ВЫДАЧА МАТЕРИАЛА ===")

# Задаём материал и количество для выдачи со склада
material_to_issue = "Шпаклёвка"
amount_to_issue = 25

if material_to_issue in warehouse:
    current_quantity = warehouse[material_to_issue]["quantity"]

    if current_quantity >= amount_to_issue:
        warehouse[material_to_issue]["quantity"] -= amount_to_issue
        print(f"Выдано {amount_to_issue} единиц: '{material_to_issue}'")
        print(
            f"Остаток: {current_quantity} -> "
            f"{warehouse[material_to_issue]['quantity']}"
        )
    else:
        print("Недостаточно материала на складе")
else:
    print("Материал не найден")
