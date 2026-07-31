import json
products = []
def add_product(products):
    category = input("Выберите категорию: ")
    name = input("Название продукта: ")
    weight = input("Введите объем(формат: число единица измерения): ")
    date = input("Срок годности(дд.мм.гг-дд.мм.гг): ")
    product = {
        "category": category,
        "name": name,
        "weight" : weight,
        "date": date
    }
    products.append(product)

def show_products(products):
    for number, product in enumerate(products,1):
        print(f"{number}.")
        print(f'Категория: {product["category"]}')
        print(f'Название: {product["name"]}')
        print(f'Объем: {product["weight"]}')
        print(f'Срок годности: {product["date"]}')
        
def find_product(products):
    search = input("Введите продукт для поиска: ")

    found = False

    for product in products:
        if search == product["name"]:
            found = True

            print("Продукт найден!")
            print(f'Категория: {product["category"]}')
            print(f'Название: {product["name"]}')
            print(f'Объем: {product["weight"]}')
            print(f'Срок годности: {product["date"]}')

            break

    if found == False:
        print("Такого продукта нет.")
            
    

def delete_product(products):
    deleting = input("Введите название продукта: ")

    found = False

    for product in products:
        if deleting == product["name"]:
            products.remove(product)
            found = True
            print("Продукт удалён.")
            break

    if found == False:
        print("Такого продукта нет.")
            
def save_products(products):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)
def load_products():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
    
products = load_products()     

while True:
    move = input("Что вы хотите сделать?( add/show/find/delete/exit): ")
    if move == "add":
        add_product(products)
        save_products(products)
    elif move == "show":
        show_products(products)
    elif move == "find":
        find_product(products)
    elif move == "delete":
        delete_product(products)
        save_products(products)
    elif move == "exit":
        break