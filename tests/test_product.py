from src.product import Product, Category

def test_product(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_category(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и " "получения дополнительных функций для удобства жизни"
    )

    assert isinstance(first_category.product_in, list)
    assert len(first_category.product_in) == 0
    assert first_category.category_count == 1

def test_prod_create():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = "180000.0"
    product.quantity = 5

new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})

# def test_new_product():
#     product = Product.new_product(new_product)
#     assert product.name == "Samsung Galaxy S23 Ultra"
#     assert product.name == "Samsung Galaxy S23 Ultra"
#     assert product.description == "256GB, Серый цвет, 200MP камера"
#     assert product.price == "180000.0"
#     assert product.quantity == 5

def test_get_price():
    product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    assert product.price == 123000.0

def test_set_price():
    product = Product("Test", "Description", 100, 10)
    product.price = 150
    assert product.price == 150

    product.price = -50
    assert product.price == 150  # Цена не должна измениться