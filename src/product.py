from unicodedata import category


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не будет быть добавлен")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, new_product: dict):
        """Взвращает созданный объект класса Product из параметров товара в словаре"""
        # name = new_product["name"]
        # description = new_product["description"]
        # price = new_product["price"]
        # quantity = new_product["quantity"]
        # return cls(name, description, price, quantity)
        return cls(**new_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if float(new_price) == 0 or float(new_price) < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        return f"{self.name}, Количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.category_count += 1

    @property
    def products(self):
        product_list = ""
        for product in self.__products:
            product_list += f"{str(product)}"
        return product_list

    @property
    # для тестов
    def product_in(self):
        return self.__products
