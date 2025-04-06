import json
import os

from src.product import Product, Category


def read_json(patch: str) -> dict:
    """Функция читает и создает объекты классов"""

    full_patch = os.path.abspath(patch)
    with open(full_patch, "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def create_ob(data):
    users = []
    for user in data:
        tasks = []
        for task in user["products"]:
            tasks.append(Product(**task))
        user["products"] = tasks
        users.append(Category(**user))
    return users


if __name__ == "__main__":
    raw = read_json("../data/products.json")
    us = create_ob(raw)
    print(us[0].name)
