import json
import time

class Pasta:
    """Модель для создания заказов в кафе с пастой так и на сайте """
    def __init__(self, name: str, ingredients: list, price: float, weight: float, picture,  additional_ingredients: list = None):
        """Метод-конструктор модели принимает данные о заказе ,заполняет необходимые поля , возвращает объект класса  """
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price
        self.__weight = weight
        self.__picture = picture
        self.__additional_ingredients = additional_ingredients if additional_ingredients is not None else []

    # Геттеры
    """Написаны  getters для полей класса  Pasta"""

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def get_picture(self):
        return self.__picture

    def get_additional_ingredients(self):
        return self.__additional_ingredients

    # Сеттеры
    """Написаны  сеттеры для остальных полей"""

    def set_price(self, new_price):
        self.__price = new_price

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def set_picture(self, new_picture):
        self.__picture = new_picture

    def set_ingredients(self, new_ingredient: list):
        """Сеттер для установки новых ингридиентов, перед тем как добавить новые очищает список старых """
        if type(new_ingredient) is list:
            self.__ingredients.clear()
            self.__ingredients.extend(new_ingredient)
        else:
            return "Ошибка не верный тип данных"

    def add_additional_ingredient(self):
        """Метод для дополнения дополнительных ингридиентов от клиентов  если они есть """
        if self.__additional_ingredients:
            self.__ingredients.extend(self.__additional_ingredients)

    def make_pasta(self):
        """Метод для изготовления пасты,
                обращается к методу get_ingredients()
                обращается к методу get_price()
                обращается к методу get_weight()
            Проверяет наличие дополнительных ингридиентов
        если есть:
            применяет метод additional_ingredients() после чего собирает заказ по заданным параментрам
        если нет
            просто собирает заказ  по переданам при инцилизации параметрам
                возращает заказанное блюдо
        """
        additional_ingredients =  self.get_additional_ingredients()
        all_ingredients = self.get_ingredients()
        price = self.get_price()
        weight = self.get_weight()
        if  additional_ingredients:
            self.add_additional_ingredient()
            all_ingredients = self.get_ingredients()
            price = price + len(additional_ingredients) * 10
            weight = weight + len(additional_ingredients) * 50
        ordered_pasta = {
            'name':self.get_name(),
            'ingredients':all_ingredients,
            'price':price,
            'weight':weight
        }
        return ordered_pasta

    def save_order_to_json(self, order):
        """Метод  для сохранения информации о заказе в файл формата .json
         принимает название заказа на его основе с учетом времени заказа
         формирует имя файла, после чего  сохраняет заказ в файл
         Возвращает сообщение  о ом какой заказ  и где сохранен"""
        ordered_pasta = self.make_pasta()
        filename = fr'orders\{round(time.time(),2)}_{order}.json'
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(ordered_pasta, fp, ensure_ascii=False, indent=2)
        return f"Заказ сохранён{order} сохранён в файл {filename}"

    def get_data_from_json(self, filename):
        """Метод  чтения информации из сохраненого файла, принимает имя файла
         преобразовывыет данные в формат понятный python, возвращает преобразованые"""
        with open(fr"{filename}.json",'r', encoding="utf-8")as fp:
            python_data = json.load(fp)
        return python_data

