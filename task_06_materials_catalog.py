# Исходный список отделочных материалов
materials = ["Гипсокартон", "Шпаклёвка", "Грунтовка", "Плитка", "Ламинат"]

print("=== КАТАЛОГ МАТЕРИАЛОВ ===")
print(f"Исходный список: {materials}")
print(f"Первый материал: {materials[0]}")
print(f"Последний материал: {materials[-1]}")
print(f"Средние элементы: {materials[1:4]}")

# Добавляем в каталог ещё две позиции для ремонта
materials.append("Краска")
materials.append("Плинтус")

print()
print("После добавления двух материалов:")
print(materials)

# Удаляем второй элемент, чтобы показать работу метода pop
deleted_material = materials.pop(1)

print()
print(f"Удалённый второй элемент: {deleted_material}")
print(f"Итоговый список: {materials}")
print(f"Длина списка: {len(materials)}")
