# Размеры комнаты в метрах
room_length = 6.8
room_width = 4.3
room_height = 2.9

# Стоимость покраски одного квадратного метра стены
paint_price = 175

# Считаем площадь пола, суммарную площадь стен и объём помещения
floor_area = room_length * room_width
wall_area = 2 * (room_length + room_width) * room_height
room_volume = room_length * room_width * room_height

# Определяем, сколько будет стоить покрасить все стены
painting_cost = wall_area * paint_price

print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Длина: {room_length} м")
print(f"Ширина: {room_width} м")
print(f"Высота: {room_height} м")
print()
print(f"Площадь пола: {floor_area:.2f} м²")
print(f"Площадь стен: {wall_area:.2f} м²")
print(f"Объём помещения: {room_volume:.2f} м³")
print(f"Стоимость покраски стен: {painting_cost:.2f} руб.")
