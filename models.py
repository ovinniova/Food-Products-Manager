from datetime import date
class Product:
    def __init__(self, category, name, quantity, unit,expiration_date):
        self.category = category
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.expiration_date = expiration_date

    def show_info(self):
            print(f'Категория: {self.category}')
            print(f'Название: {self.name}')
            print(f"Количество: {self.quantity} {self.unit}")
            print(f'Срок годности: {self.expiration_date} ')
            self.show_expiration_status()

    def use(self, amount):
        if amount > self.quantity:
            print("Недостаточное количество продукта")
            return

        self.quantity = self.quantity - amount

        if self.quantity == 0:
            print("Продукт закончился")
        else:
            print(f"Осталось: {self.quantity} {self.unit}")

    def to_dict(self):
         return {
              "category": self.category,
              "name" : self.name,
              "quantity": self.quantity,
              "unit": self.unit,
              "expiration_date": self.expiration_date
         }
    
    def show_expiration_status(self):
        difference = self.expiration_date - date.today()
        days_left = difference.days
        if days_left < 0:
            print("Продукт просрочен.")
        elif days_left == 0:
            print("Последний день срока годности. Съешьте скорее!")
        elif 1 <= days_left <= 3:
            print("Срок скоро истечет")
        else:
            print("Продукт еще свежий")
        