from classes.menu import MenuComponent


def user_flow(menu_instance):
    menu_instance.print_menu_items()
    menu_instance.user_input()
    menu_instance.console_clear()

    selected_func = menu_instance.select_menu_item(menu_instance.get_selected_menu_item())
    selected_func()

    user_flow(menu_instance)


def main():
    menu = MenuComponent()
    menu.console_clear()
    user_flow(menu)


if __name__ == '__main__':
    main()
