class Product:
    """Вспомогательный класс товара"""
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

class WarehouseManager:
    """
    ЗАДАЧА: Логика склада.
    1. add_product(product): добавляет объект Product в self.items.
    2. filter_by_category(cat): возвращает список ОБЪЕКТОВ только этой категории.
    3. get_total_value(): возвращает сумму цен всех товаров на складе (float/int).
    """
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def filter_by_category(self, category: str):
        filtered_items = []
        for item in self.items:
            if item.category == category:
                filtered_items.append(item)
        return filtered_items

    def get_total_value(self):
        return sum([item.price for item in self.items])