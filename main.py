import json
import os
from datetime import datetime

# здесь был 561138
FILE_NAME = "finance.json"


# Загрузка данных
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


# Сохранение данных
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Добавление операции
def add_operation(data):
    print("\n===== ДОБАВЛЕНИЕ ОПЕРАЦИИ =====")

    operation_type = input("Тип операции (доход/расход): ").lower()

    if operation_type not in ["доход", "расход"]:
        print("Ошибка: нужно написать «доход» или «расход».")
        return

    try:
        amount = float(input("Сумма: "))

        if amount <= 0:
            print("Сумма должна быть больше 0.")
            return

    except ValueError:
        print("Ошибка: введите число.")
        return

    category = input("Категория: ")

    comment = input("Комментарий: ")

    operation = {
        "type": operation_type,
        "amount": amount,
        "category": category,
        "comment": comment,
        "date": datetime.now().strftime("%d.%m.%Y %H:%M")
    }

    data.append(operation)
    save_data(data)

    print("Операция успешно добавлена!")


# Показ всех операций
def show_operations(data):
    print("\n===== ВСЕ ОПЕРАЦИИ =====")

    if len(data) == 0:
        print("Операций пока нет.")
        return

    for i, operation in enumerate(data, 1):
        print(
            f"{i}. {operation['date']} | "
            f"{operation['type']} | "
            f"{operation['amount']:.2f} ₽ | "
            f"{operation['category']} | "
            f"{operation['comment']}"
        )

# здесь был 561004
# Расчёт основных показателей
def calculate_statistics(data):
    income = 0
    expenses = 0

    for operation in data:
        if operation["type"] == "доход":
            income += operation["amount"]
        else:
            expenses += operation["amount"]

    balance = income - expenses

    return income, expenses, balance


# Статистика
def show_statistics(data):
    print("\n===== ФИНАНСОВАЯ СТАТИСТИКА =====")

    if len(data) == 0:
        print("Недостаточно данных.")
        return

    income, expenses, balance = calculate_statistics(data)

    print(f"Общий доход:   {income:.2f} ₽")
    print(f"Общие расходы: {expenses:.2f} ₽")
    print(f"Баланс:        {balance:.2f} ₽")

    expense_operations = [
        operation for operation in data
        if operation["type"] == "расход"
    ]

    if len(expense_operations) > 0:

        # Расходы по категориям
        categories = {}

        for operation in expense_operations:
            category = operation["category"]

            if category not in categories:
                categories[category] = 0

            categories[category] += operation["amount"]

        print("\nРасходы по категориям:")

        for category, amount in categories.items():
            print(f"- {category}: {amount:.2f} ₽")

        # Самая большая категория
        max_category = max(categories, key=categories.get)

        print(
            f"\nСамая затратная категория: "
            f"{max_category} — {categories[max_category]:.2f} ₽"
        )

        # Средний расход
        average_expense = expenses / len(expense_operations)

        print(f"Средний расход: {average_expense:.2f} ₽")

    # Финансовая оценка
    print("\n===== ОЦЕНКА =====")

    if balance > 0:
        print("Ваш баланс положительный.")

    elif balance == 0:
        print("Доходы равны расходам.")

    else:
        print("Внимание! Расходы превышают доходы.")


# Удаление операции
def delete_operation(data):
    show_operations(data)

    if len(data) == 0:
        return

    try:
        number = int(input("\nВведите номер операции для удаления: "))

        if number < 1 or number > len(data):
            print("Такой операции нет.")
            return

        deleted = data.pop(number - 1)

        save_data(data)

        print(
            f"Операция «{deleted['category']} "
            f"{deleted['amount']:.2f} ₽» удалена."
        )

    except ValueError:
        print("Введите целое число.")


# Главное меню
def main():
    data = load_data()

    while True:
        print("\n")
        print("======================================")
        print("       АНАЛИЗАТОР ЛИЧНЫХ ФИНАНСОВ")
        print("======================================")
        print("1. Добавить операцию")
        print("2. Показать операции")
        print("3. Финансовая статистика")
        print("4. Удалить операцию")
        print("5. Выход")
        print("======================================")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_operation(data)

        elif choice == "2":
            show_operations(data)

        elif choice == "3":
            show_statistics(data)

        elif choice == "4":
            delete_operation(data)

        elif choice == "5":
            print("\nСпасибо за использование программы!")
            break

        else:
            print("Ошибка: выберите пункт от 1 до 5.")


# Запуск программы
if __name__ == "__main__":
    main()
    #  Сделал изменения 561223
