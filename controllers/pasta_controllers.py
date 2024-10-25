import os

class PastaController:
    """Класс контролер для передачи информации от модели на представление """
    def __init__(self, model):
        """Метод конструктор инциализируется экземпляром класса Pasta  """
        self.model = model

    def menu_cafe(self):
        """Метод для передачи данных по меню """
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                      f"Состав :: {','.join(self.model.get_ingredients())}\n"
                      f"Цена :: {self.model.get_price()}\n"
                      f"Вес :: {self.model.get_weight()}\n")
        return pasta_data

    def site_menu(self):
        """Метод для передачи данных для меню на сайте """
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                      f"Состав :: {','.join(self.model.get_ingredients())}\n"
                      f"Цена :: {self.model.get_price()}\n"
                      f"Вес :: {self.model.get_weight()}\n"
                      f"Фото :: {os.startfile(self.model.get_picture())}")
        return pasta_data

    """Методы set_ingredients, set_price, set_weight,  set_picture предназначены для передачи информации по соответствующим данным  от представления модели
            получает права доступа пользователя , данные необходимого типа   ( тип ланных проверяется на этапе view)
             Проверяют права доступа
             если права доступа  подходят  - данные  для изменения отправляются в модель
             если права доступа не подходят  - выдают соответствующее сообщение """
    def set_ingredients(self, user_right, new_ingredients):
        if user_right in["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_ingredients(new_ingredients)
            return "Новый рецепт!"
        else:
            return "banned"

    def set_price(self, user_right, new_price):
        if user_right in["Admin", "IsStaff", "IsSuperuser"]:
            price_int = int(new_price)
            self.model.set_price(new_price)
            return "Цена изменена"
        else:
            return "banned"

    def set_weight(self, user_right, new_weight):
        if user_right in["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_weight(new_weight)
            return "Вес изменен"
        else:
            return "banned"

    def set_picture(self, user_right, new_picture):
        if user_right in["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_picture(new_picture)
            return "Картинка изменена"
        else:
            return "banned"

    def save_order_to_json(self, order):
        """Реализует функционал сохранения модели """
        return  self.model.save_order_to_json(order)

    def get_data_from_json(self, user_right, filename):
        """Получсет от пользователя права и мия файла
         Проверяет права доступа
            если права доступа  подходят  - передает информацию  о заказе
             если права доступа не подходят  - выдает соответствующее сообщение"""
        if user_right in ["Admin", "IsStaff", "IsSuperuser"]:
            return  self.model.get_data_from_json(filename)
        else:
            return "banned"