# Считываем номер дня недели от пользователя
weekday_number = int(input("Введите номер дня недели: "))

# Подбираем текстовое название дня
if weekday_number == 1:
    weekday_name = "Понедельник"
elif weekday_number == 2:
    weekday_name = "Вторник"
elif weekday_number == 3:
    weekday_name = "Среда"
elif weekday_number == 4:
    weekday_name = "Четверг"
elif weekday_number == 5:
    weekday_name = "Пятница"
elif weekday_number == 6:
    weekday_name = "Суббота"
elif weekday_number == 7:
    weekday_name = "Воскресенье"
else:
    weekday_name = "Некорректный номер дня"

# Определяем режим работы в зависимости от номера дня
if 1 <= weekday_number <= 5:
    day_status = "Рабочий день"
    schedule_mode = "8:00 - начало смены"
elif weekday_number == 6 or weekday_number == 7:
    day_status = "Выходной"
    schedule_mode = "Отдых"
else:
    day_status = "Не определён"
    schedule_mode = "Проверьте номер дня"

print("=== РАБОЧИЙ ГРАФИК ===")
print(f"Номер дня: {weekday_number}")
print(f"День недели: {weekday_name}")
print(f"Статус: {day_status}")
print(f"Режим: {schedule_mode}")
