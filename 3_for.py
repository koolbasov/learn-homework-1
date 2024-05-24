"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

all_phone_sales = [
    {
        "product": "iPhone 12",
        "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
    },
    {
        "product": "Xiaomi Mi11",
        "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
    },
    {
        "product": "Samsung Galaxy 21",
        "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
    },
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    for product in all_phone_sales:
        print(
            f"Cуммарное количество продаж для {product['product']}: "
            f"{sum(product['items_sold'])}"
        )
    all_sales_sum = 0
    count_sales = 0
    for product in all_phone_sales:
        print(
            f"Среднее количество продаж {product['product']}: "
            f"{round(sum(product['items_sold']) / len(product['items_sold']), 2)}"
        )
        count_sales += len(product["items_sold"])
        all_sales_sum += sum(product["items_sold"])

    print(f"Cуммарное количество продаж всех товаров: {all_sales_sum}")
    print(f"Cреднее количество продаж всех товаров: {all_sales_sum / count_sales}")


if __name__ == "__main__":
    main()
