# Данные исполнителя
fio_student = "Шорохова Александра Андреевна"
group_code = "52501"

# Краткие сведения о строительном объекте
project_name = 'ЖК "Северный квартал"'
floors = 17
height = 54
is_residential = True
construction_year = 2021

# Для вывода превращаем логическое значение в понятный текст
object_type = "Жилой" if is_residential else "Нежилой"

print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {fio_student}")
print(f"Группа: {group_code}")
print()
print(f"Объект: {project_name}")
print(f"Этажность: {floors} этажей")
print(f"Высота: {height} м")
print(f"Тип: {object_type}")
print(f"Год постройки: {construction_year}")

# Адрес объекта:
# г. Новосибирск, ул. Тюленина, д. 26
# Причина выбора:
# современный жилой комплекс, для которого удобно показать параметры здания
