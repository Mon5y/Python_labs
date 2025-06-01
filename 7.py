import json
from jsonschema import validate, ValidationError

# task 1
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "movies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "year": {"type": "integer"},
                    "cast": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "role": {"type": "string"}
                            },
                            "required": ["name", "role"]
                        }
                    }
                },
                "required": ["title", "year", "cast"]
            }
        }
    },
    "required": ["movies"]
}


with open('ex_1.json') as f:
    valid_data = json.load(f)


invalid_data = valid_data.copy()
invalid_data["movies"][0]["year"] = "1999"  

def validate_json(data):
    try:
        validate(instance=data, schema=schema)
        return "✅ Файл валиден"
    except ValidationError as e:
        return f"❌ Ошибка валидации: {e.message}"


with open('ex_1_invalid.json', 'w') as f:
    json.dump(invalid_data, f, indent=2)


print("===== ЗАДАНИЕ 1 =====")
print("Проверка исходного файла:", validate_json(valid_data))
print("Проверка ошибочного файла:", validate_json(invalid_data))
print("Ошибочный файл сохранен как 'ex_1_invalid.json'\n")

# task 2 
# Исправление формата файла (добавляем скобки для массива)
with open('ex_2.json') as f:
    raw_content = f.read().strip()
    corrected_content = f'[{raw_content.replace("}{", "},{")}]'
    user_data = json.loads(corrected_content)


with open('ex_2_pretty.json', 'w') as f:
    json.dump(user_data, f, indent=2)


user_phone_dict = {user["name"]: user["phoneNumber"] for user in user_data}

print("===== ЗАДАНИЕ 2 =====")
print("Читабельный файл сохранен как 'ex_2_pretty.json'")
print("Словарь пользователей (имя → телефон):")
for name, phone in user_phone_dict.items():
    print(f"- {name}: {phone}")
print()

# task 3

with open('ex_3.json') as f:
    invoice_data = json.load(f)

new_invoice = {
    "id": 3,
    "total": 150.50,
    "items": [
        {"name": "item 4", "quantity": 3, "price": 30.00},
        {"name": "item 5", "quantity": 2, "price": 30.25}
    ]
}

invoice_data["invoices"].append(new_invoice)

with open('ex_3_updated.json', 'w') as f:
    json.dump(invoice_data, f, indent=2)

print("===== ЗАДАНИЕ 3 =====")
print("Обновлённый файл сохранён как 'ex_3_updated.json'")
print("Добавлен новый счёт:")
print(json.dumps(new_invoice, indent=2))