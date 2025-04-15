import pytest


def test_smart(product_smart1):
    assert product_smart1.name == "Samsung Galaxy S23 Ultra"
    assert product_smart1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smart1.price == 180000.0
    assert product_smart1.quantity == 5
    assert product_smart1.efficiency == 95.5
    assert product_smart1.memory == 256
    assert product_smart1.color == "Серый"


def test_smart_add(product_smart1, product_smart2):
    assert product_smart1 + product_smart2 == 1800000.0


def test_smart_add_error(product_smart1, product_smart2):
    with pytest.raises(TypeError):
        res = product_smart1 + 1


def test_lawn(product_Lawn1):
    assert product_Lawn1.name == "Газонная дорожка"
    assert product_Lawn1.description == "Элитная трава для газона"
    assert product_Lawn1.price == 500.0
    assert product_Lawn1.quantity == 20
    assert product_Lawn1.country == "Россия"
    assert product_Lawn1.germination_period == "7 дней"
    assert product_Lawn1.color == "Зеленый"


def test_Lown_add(product_Lawn1, product_Lawn2):
    assert product_Lawn1 + product_Lawn1 == 20000.0


def test_Lown_add_error(product_Lawn1, product_Lawn2):
    with pytest.raises(TypeError):
        res = product_Lawn1 + 1
