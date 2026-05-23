# Цена одного мешка сухой смеси и число мешков в заказе
unit_price = 720
item_count = 7

# Находим полную стоимость заказа до применения скидки
order_total = unit_price * item_count

# Выбираем процент скидки по сумме заказа
if order_total < 1000:
    discount_percent = 0
elif order_total <= 5000:
    discount_percent = 5
else:
    discount_percent = 10

# Считаем размер скидки и сумму, которую нужно оплатить
discount_amount = order_total * discount_percent / 100
final_total = order_total - discount_amount

print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {unit_price:.2f} руб.")
print(f"Количество товара: {item_count}")
print(f"Стоимость без скидки: {order_total:.2f} руб.")
print(f"Размер скидки: {discount_percent}%")
print(f"Сумма скидки: {discount_amount:.2f} руб.")
print(f"Итоговая стоимость: {final_total:.2f} руб.")

# Пример покупки:
# в заказ включено 7 мешков сухой смеси по 720 рублей.
#
# Почему выбраны такие числа:
# итоговая сумма превышает 5000 рублей, поэтому срабатывает скидка 10%.
