from datetime import datetime

from categories import choose_category
from models import Product


def add_product(products):
    category = choose_category()

    name = input(
        "Название продукта: "
    ).strip()

    try:
        quantity = float(
            input("Количество продукта: ")
        )

    except ValueError:
        print(
            "Количество необходимо "
            "вводить числом."
        )
        return

    if quantity <= 0:
        print(
            "Количество должно быть "
            "больше нуля."
        )
        return

    unit = input(
        "Единица измерения: "
    ).strip()

    expiration_text = input(
        "Срок годности "
        "(дд.мм.гггг): "
    )

    try:
        expiration_date = (
            datetime.strptime(
                expiration_text,
                "%d.%m.%Y"
            ).date()
        )

    except ValueError:
        print(
            "Неверный формат даты. "
            "Пример: 25.08.2026"
        )
        return

    product = Product(
        category=category,
        name=name,
        quantity=quantity,
        unit=unit,
        expiration_date=expiration_date
    )

    products.append(product)

    print("Продукт добавлен.")


def show_products(products):
    if not products:
        print("Список продуктов пуст.")
        return

    for number, product in enumerate(
        products,
        1
    ):
        print(f"\n--- {number} ---")
        product.show_info()


def find_product(products):
    search = input(
        "Введите название продукта: "
    ).strip()

    for product in products:
        if (
            search.lower()
            == product.name.lower()
        ):
            print("Продукт найден.")
            product.show_info()
            return

    print("Такого продукта нет.")


def use_product(products):
    product_name = input(
        "Какой продукт использовать: "
    ).strip()

    for product in products:
        if (
            product_name.lower()
            == product.name.lower()
        ):
            try:
                amount = float(
                    input(
                        f"Сколько использовать "
                        f"({product.unit}): "
                    )
                )

            except ValueError:
                print(
                    "Количество необходимо "
                    "вводить числом."
                )
                return

            product.use(amount)
            return

    print("Такого продукта нет.")


def delete_product(products):
    deleting = input(
        "Введите название продукта: "
    ).strip()

    for product in products:
        if (
            deleting.lower()
            == product.name.lower()
        ):
            products.remove(product)

            print("Продукт удалён.")
            return

    print("Такого продукта нет.")