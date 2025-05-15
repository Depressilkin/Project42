from model import Basket, PizzaBase, PizzaMargarita, PizzaPepperoni, PizzaHawaii, Topping, Recipe, Controller
class Menu:
    def __init__(self):
        self.basket = None
        self.controller = Controller()

    def start_menu(self):
        self.basket = Basket()
        topping = Topping()
        while True:
            print('Меню:')
            menu = input('1-Создать заказ\n2-Статистика')
            if menu == '1':
                while True:
                    menu = input('1-Маргарита\n2-Пепперони\n3-Гавайская\n4-свой рецепт')
                    if menu == '1':
                        order_topping = topping.add_topping()    
                        pizza = PizzaMargarita('Маргарита', 670, order_topping)
                    elif menu == '2':
                        order_topping = topping.add_topping()
                        pizza = PizzaPepperoni('Пепперони', 780, order_topping)
                    elif menu == '3':
                        order_topping = topping.add_topping()
                        pizza = PizzaHawaii('Гавайская', 1080, order_topping)
                    elif menu == '4':
                        order_topping = topping.add_topping()
                        recipe = Recipe()
                        order_recipe = recipe.create_recipe()
                        name = input('Назовите свой рецепт')
                        pizza = PizzaBase(name, 120, order_topping)
                        pizza.set_recipe(order_recipe)
                    self.basket.add_order(pizza)
                    print(f'Корзина: {self.basket.basket_summa} rub')
                    menu = input('1-продолжить заказ\n2-перейти в корзину')
                    if menu == '1':
                        continue
                    else:
                        self.get_basket()
                        break
            elif menu == '2':
                print(self.controller.get_statistic())


    def get_basket(self):
        print('Cостав заказа:', self.basket.get_list_order(), 'Cумма заказа:' + str(self.basket.get_summa()) + 'rub', sep='\n')
        menu = input('1-подтвертить\n2-назад')
        if menu == '1':
            self.controller.basket_counter(self.basket)
            self.start_menu()
        else:
            return False
