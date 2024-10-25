import os
from models.pasta_model import pasta_model
from controllers.pasta_controllers import pasta_controllers
from views.pasta_view import pasta_view

if __name__ == "__main__":
    image_path = os.path.abspath('image/karbonara.jpg')
    my_model = pasta_model(
       name = 'Паста карбонара',
       ingredients = ["спагетти", "бекон", "пармезан", "чёрный перец", "соль", "оливковое масло", "яичные желтки"],
       price = 450 ,
       weight = 600,
       picture =  image_path,
       additional_ingredients = ["+макароны", "+бекон", "+пармезана"]
    )
    my_controller = pasta_controllers(my_model)
    my_view = pasta_view(my_controller)
    my_view.show_cafe_menu()
    my_view.show_site_menu()
    my_view.save_order_to_json("Паста карбонара_+")
    #my_view.get_data_from_json('Admin', r'orders\1827407360.54_карбонара_Стандарт')
    print()
    my_view.set_ingredients('user', ["спагетти", "бекон", "пармезан", "оливковое масло", "яичные желтки"])
    my_view.set_ingredients('Admin', ("спагетти", "бекон", "пармезан", "оливковое масло", "яичные желтки"))
    my_view.set_ingredients('Admin', ["спагетти", "бекон", "пармезан", "оливковое масло", "яичные желтки"])
    print()
    my_view.set_price('user', "550")
    my_view.set_price('Admin', "пятьсот пятьдесят")
    my_view.set_price('Admin', "550")
    print()
    my_view.set_weight('user', "550")
    my_view.set_weight('Admin', "пятьсот пятьдесят")
    my_view.set_weight('Admin', "550")
    print()
    my_view.show_cafe_menu()




