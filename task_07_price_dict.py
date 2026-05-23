# Словарь с ценами на отделочные материалы
price_catalog = {
    "Гипсокартон": 410.0,
    "Шпаклёвка": 365.0,
    "Грунтовка": 290.0,
    "Плитка": 1380.0,
    "Ламинат": 1250.0,
}

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
print(f"Исходный словарь: {price_catalog}")

# Добавляем две новые позиции в прайс-лист
price_catalog["Краска"] = 760.0
price_catalog["Плинтус"] = 185.0

print()
print("После добавления двух материалов:")
print(price_catalog)

# Повышаем цену грунтовки на 10 процентов
price_catalog["Грунтовка"] = price_catalog["Грунтовка"] * 1.10

# Форматируем цены для более аккуратного вывода
formatted_catalog = {
    material_name: f"{material_price:.2f}"
    for material_name, material_price in price_catalog.items()
}

print()
print("После изменения цены грунтовки на 10%:")
print(formatted_catalog)

# Удаляем одну позицию из словаря и запоминаем её цену
removed_price = price_catalog.pop("Плинтус")
formatted_catalog = {
    material_name: f"{material_price:.2f}"
    for material_name, material_price in price_catalog.items()
}

print()
print(f"Удалённый материал: Плинтус ({removed_price:.2f} руб.)")
print(f"Итоговый словарь: {formatted_catalog}")

# Считаем среднюю цену оставшихся материалов
average_price = sum(price_catalog.values()) / len(price_catalog)

print(f"Средняя цена материалов: {average_price:.2f} руб.")
