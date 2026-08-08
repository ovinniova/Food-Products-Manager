CATEGORIES = {
    "Мясо": {
        "Птица": [
            "Курица",
            "Индейка",
            "Утка"
        ],
        "Красное мясо": [
            "Говядина",
            "Свинина",
            "Баранина"
        ]
    },

    "Молочные продукты": [
        "Молоко",
        "Сыр",
        "Йогурт",
        "Творог",
        "Сметана",
        "Сливки"
    ],

    "Овощи": [
        "Картофель",
        "Морковь",
        "Помидоры",
        "Огурцы",
        "Лук"
    ],

    "Фрукты": [
        "Яблоки",
        "Бананы",
        "Апельсины",
        "Груши"
    ],

    "Крупы и макароны": [
        "Рис",
        "Гречка",
        "Овсянка",
        "Макароны"
    ],

    "Напитки": [
        "Вода",
        "Сок",
        "Чай",
        "Кофе"
    ],

    "Сладости": [
        "Шоколад",
        "Конфеты",
        "Печенье"
    ]
}


def choose_from_list(items):
    for number, item in enumerate(items, 1):
        print(f"{number}. {item}")

    while True:
        try:
            choice = int(
                input("Введите номер: ")
            )

            if 1 <= choice <= len(items):
                return items[choice - 1]

            print("Такого номера нет.")

        except ValueError:
            print("Введите число.")


def choose_category():
    main_categories = list(CATEGORIES.keys())

    print("\nВыберите категорию:")
    main_category = choose_from_list(
        main_categories
    )

    category_data = CATEGORIES[main_category]

    if isinstance(category_data, list):
        print("\nВыберите подкатегорию:")

        product_type = choose_from_list(
            category_data
        )

        return (
            f"{main_category} > "
            f"{product_type}"
        )

    subcategories = list(
        category_data.keys()
    )

    print("\nВыберите подкатегорию:")
    subcategory = choose_from_list(
        subcategories
    )

    product_types = category_data[
        subcategory
    ]

    print("\nВыберите тип продукта:")
    product_type = choose_from_list(
        product_types
    )

    return (
        f"{main_category} > "
        f"{subcategory} > "
        f"{product_type}"
    )