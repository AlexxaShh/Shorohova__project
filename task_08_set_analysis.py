# Списки материалов, которые заказали три разные бригады
crew_1 = ["Гипсокартон", "Грунтовка", "Краска", "Ламинат"]
crew_2 = ["Грунтовка", "Плитка", "Краска", "Плинтус"]
crew_3 = ["Грунтовка", "Краска", "Обои", "Гипсокартон"]

# Преобразуем списки в множества для операций сравнения
set_1 = set(crew_1)
set_2 = set(crew_2)
set_3 = set(crew_3)

# Находим все уникальные, общие и частично совпадающие материалы
all_materials = set_1 | set_2 | set_3
common_materials = set_1 & set_2 & set_3
only_first_crew = set_1 - set_2 - set_3
shared_by_two = (set_1 & set_2) | (set_1 & set_3) | (set_2 & set_3)
shared_by_two = shared_by_two - common_materials

print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Материалы первого подрядчика: {crew_1}")
print(f"Материалы второго подрядчика: {crew_2}")
print(f"Материалы третьего подрядчика: {crew_3}")
print()
print(f"Все уникальные материалы: {sorted(all_materials)}")
print(f"Общие для всех: {sorted(common_materials)}")
print(f"Только у первого подрядчика: {sorted(only_first_crew)}")
print(f"Ровно у двух подрядчиков: {sorted(shared_by_two)}")
