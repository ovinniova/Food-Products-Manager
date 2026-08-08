import json
from datetime import date

from models import Product


FILE_NAME = "data.json"


def save_products(products):
    products_as_dicts = []

    for product in products:
        product_dict = {
            "category": product.category,
            "name": product.name,
            "quantity": product.quantity,
            "unit": product.unit,
            "expiration_date":
                product.expiration_date.isoformat()
        }

        products_as_dicts.append(
            product_dict
        )

    with open(
        FILE_NAME,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            products_as_dicts,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_products():
    try:
        with open(
            FILE_NAME,
            "r",
            encoding="utf-8"
        ) as file:
            products_as_dicts = json.load(
                file
            )

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print(
            "data.json пуст или повреждён."
        )
        return []

    products = []

    for product_dict in products_as_dicts:
        try:
            expiration_date = (
                date.fromisoformat(
                    product_dict[
                        "expiration_date"
                    ]
                )
            )

            product = Product(
                category=product_dict[
                    "category"
                ],
                name=product_dict["name"],
                quantity=float(
                    product_dict["quantity"]
                ),
                unit=product_dict["unit"],
                expiration_date=expiration_date
            )

            products.append(product)

        except (
            KeyError,
            ValueError,
            TypeError
        ):
            print(
                "Пропущена повреждённая "
                "запись из data.json."
            )

    return products