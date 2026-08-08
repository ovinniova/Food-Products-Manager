from products import (
    add_product,
    delete_product,
    find_product,
    show_products,
    use_product
)

from storage import (
    load_products,
    save_products
)


products = load_products()


while True:
    print(
        "\n"
        "add    — добавить\n"
        "show   — показать\n"
        "find   — найти\n"
        "use    — использовать\n"
        "delete — удалить\n"
        "exit   — выйти"
    )

    move = input(
        "\nВыберите действие: "
    ).strip().lower()

    if move == "add":
        add_product(products)
        save_products(products)

    elif move == "show":
        show_products(products)

    elif move == "find":
        find_product(products)

    elif move == "use":
        use_product(products)
        save_products(products)

    elif move == "delete":
        delete_product(products)
        save_products(products)

    elif move == "exit":
        save_products(products)
        print("Данные сохранены.")
        break

    else:
        print("Неизвестная команда.")