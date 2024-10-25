class PastaView:
    def __init__(self, controller):
        self.controller = controller

    def show_cafe_menu(self):
        print(self.controller.menu_cafe())

    def show_site_menu(self):
        print(self.controller.site_menu())

    def set_ingredients(self, user_right, new_ingredients):
        if type(new_ingredients) is not list:
            print("Неверный тип данных!")
            return
        set_ingredients_response = self.controller.set_price(user_right, new_ingredients)
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
        print(self.controller.save_order_to_json(order))

    def get_data_from_json(self,user_right,  filename):
        get_data_from_json_response = self.controller.get_data_from_json(user_right, filename)
        if get_data_from_json_response == 'banned':
            print("Нет права доступа")
        else:
            print(get_data_from_json_response)

