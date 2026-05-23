# Исходная температура воды в градусах Цельсия
celsius_temperature = 42

# Переводим значение в градусы Фаренгейта
fahrenheit_temperature = celsius_temperature * 9 / 5 + 32

# По температуре определяем агрегатное состояние воды
if celsius_temperature <= 0:
    water_state = "Лёд"
elif celsius_temperature >= 100:
    water_state = "Пар"
else:
    water_state = "Жидкость"

print("=== КОНВЕРТЕР ТЕМПЕРАТУР ===")
print(f"Температура в Цельсиях: {celsius_temperature} °C")
print(f"Температура в Фаренгейтах: {fahrenheit_temperature:.2f} °F")
print(f"Состояние воды: {water_state}")
