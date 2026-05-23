raw_addresses = [
    "  г. Казань; ул. Баумана, д. 7 ",
    "г.Самара,ул.Молодогвардейская,д.15",
    " г. Тула ; ул. Советская; д. 21  ",
]

# Сюда будем по очереди складывать уже нормализованные адреса
clean_addresses = []

for raw_address in raw_addresses:
    # Сначала удаляем лишние пробелы по краям строки
    normalized_address = raw_address.strip()
    # Затем приводим все разделители к формату с запятыми
    normalized_address = normalized_address.replace(";", ",")
    normalized_address = normalized_address.replace(", ", ",")
    normalized_address = normalized_address.replace(" ,", ",")
    # После сокращений добавляем пробелы, чтобы адрес читался единообразно
    normalized_address = normalized_address.replace("г.", "г. ")
    normalized_address = normalized_address.replace("ул.", "ул. ")
    normalized_address = normalized_address.replace("д.", "д. ")

    # Убираем двойные пробелы, если они появились после замен
    while "  " in normalized_address:
        normalized_address = normalized_address.replace("  ", " ")

    # После каждой запятой оставляем один пробел
    normalized_address = normalized_address.replace(",", ", ")

    while "  " in normalized_address:
        normalized_address = normalized_address.replace("  ", " ")

    clean_addresses.append(normalized_address.strip())

print("=== СРАВНЕНИЕ ===")

for index_address, raw_address in enumerate(raw_addresses, start=1):
    print(f"#{index_address}")
    print(f"ДО: '{raw_address}'")
    print(f"ПОСЛЕ: '{clean_addresses[index_address - 1]}'")
    print()
