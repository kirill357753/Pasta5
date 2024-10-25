class PastaView:
    """Класс для представления пользователю информации и получение данных от него   """
    def __init__(self, controller):
        """Метод конструктор инциализируется экземпляром класса PastaController  """
        self.controller = controller

    def show_cafe_menu(self):
        """Предоставляет информацию переданную  соттветсвующую контроллером   """
        print(self.controller.menu_cafe())

    def show_site_menu(self):
        """Предоставляет информацию переданную  соттветсвующую контроллером   """
        print(self.controller.site_menu())

    """Методы получения данных пользователя 
     принимают права доступа и  соответсвующие данные
    - проводят проверку на требуемый тип данных
    если данные подходят - то передают их на контроллер от которого получают тот или иной ответ 
        - если ответ положительный то выводится соответсвующее сообщение 
        если ответ отрицательный то пользователь получает ответ  "нет права доступа"
     если данные не подходят -  сообщают об этом пользователю """
    def set_ingredients(self, user_right, new_ingredients):
        if type(new_ingredients) is not list:
            print("Неверный тип данных!")
            return
        set_ingredients_response = self.controller.set_ingredients(user_right, new_ingredients)
        if set_ingredients_response == "banned":
            print("Нет права доступа")
        else:
            print(set_ingredients_response)

    def set_price(self, user_right, new_price):
        if new_price.isdigit() is False:
            print("Допустимы только циры!")
            return
        set_price_response = self.controller.set_price(user_right, new_price)
        if set_price_response == "banned":
            print("Нет права доступа")
        else:
            print(set_price_response)

    def set_weight(self, user_right, new_weight):
        if new_weight.isdigit() is False:
            print("Допустимы только циры!")
            return
        set_weight_response = self.controller.set_weight(user_right, new_weight)
        if set_weight_response == "banned":
            print("Нет права доступа")
        else:
            print(set_weight_response)

    def set_picture(self, user_right, new_picture):
        set_picture_response = self.controller.set_picture(user_right, new_picture)
        if  set_picture_response == "banned":
            print("Нет права доступа")
        else:
            print(set_picture_response)

    def save_order_to_json(self,order):
        """Метод для вывода информации о сохранение заказа    """
        print(self.controller.save_order_to_json(order))

    def get_data_from_json(self,user_right,  filename):
        """Метод для полуения информации о заказе из файла.
          Принимает права доступа  и имя файл
          если права достпуа подходят  - возвращает данные о заказе
          если права доступа не подходят - пользователь получает ответ  "нет права доступа" """
        get_data_from_json_response = self.controller.get_data_from_json(user_right, filename)
        if get_data_from_json_response == 'banned':
            print("Нет права доступа")
        else:
            print(get_data_from_json_response)

