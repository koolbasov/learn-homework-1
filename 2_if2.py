"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры
  и выводя на экран результаты

"""


def string_comparison(string1, string2):
    if isinstance(string1, str) and isinstance(string2, str):
        if string1 == string2:
            return 1
        elif len(string1) != len(string2) and string2 == "learn":
            return 3
        elif len(string1) != len(string2) and len(string1) > len(string2):
            return 2
    else:
        return 0


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(string_comparison(1, "строка"))
    print(string_comparison(1, 1))
    print(string_comparison("строка", "строка"))
    print(string_comparison("длинная строка", "строка"))
    print(string_comparison("строка", "learn"))
    # следующий вызов вернет None так как этот случай не предусмотрен в условии
    # задания
    print(string_comparison("строка", "длинная строка"))


if __name__ == "__main__":
    main()
