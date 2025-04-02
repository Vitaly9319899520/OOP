def test_product(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_category(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни"
    )

    assert isinstance(first_category.products, list)
    assert  len(first_category.products) == 0
    assert first_category.category_count == 1

