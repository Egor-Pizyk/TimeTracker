import os

from classes.tracker import TrackerComponent


class MenuComponent(TrackerComponent):
    def __init__(self):
        super().__init__()
        self.menu_items_list = None
        self._selected_menu_item = None

    def get_selected_menu_item(self):
        return self._selected_menu_item

    def print_menu_items(self):
        if self._is_countdown_start:
            self.menu_items_list = {1: ['1 - Pause work', self.pause_work],
                                    2: ['2 - Stop work', self.stop_work],
                                    3: ['3 - Show history', 0]}

        elif self._is_countdown_pause:
            self.menu_items_list = {1: ['1 - Continue work', self.continue_work],
                                    2: ['2 - Stop work', self.stop_work]}

        else:
            self.menu_items_list = {1: ['1 - Start work', self.start_work],
                                    2: ['2 - Show history', self.get_history]}

        for key, value in self.menu_items_list.items():
            print(value[0])

    @staticmethod
    def __is_value_int(value):
        try:
            int(value)
            return True

        except ValueError as ex:
            return False

    def validate_user_input(self, value):
        if self.__is_value_int(value) and int(value) in self.menu_items_list.keys():
            self._selected_menu_item = int(value)
            return True

        else:
            print('Wrong value\nWrite \'exit\' to close program')
            return False

    def user_input(self):
        value = input('\nSelect menu item: ')
        if value != 'exit':
            if not self.validate_user_input(value):
                self.user_input()
        else:
            exit(0)

    def select_menu_item(self, user_input: int):
        for key, value in self.menu_items_list.items():
            if key == user_input:
                return value[1]

    @staticmethod
    def console_clear():
        os.system('cls')
