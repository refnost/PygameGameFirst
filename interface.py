from settings import *


class Menu(InterfaceButtons):
    def __init__(self, screen, pos=(0, 0)):
        super(Menu, self).__init__(screen, pos)

    def create_buttons(self):
        screen = self.screen.get_rect().size
        self.buttons.append(MyButton(self.screen, start_game_b, (screen[0] / 2, screen[1] / 2 - 70), 3, "start"))
        self.buttons.append(MyButton(self.screen, options_b, (screen[0] / 2, screen[1] / 2), 3, "options"))
        self.buttons.append(MyButton(self.screen, exit_game_b, (screen[0] / 2, screen[1] / 2 + 70), 3, "exit"))


class MenuOptions(InterfaceButtons):
    def __init__(self, screen, pos=(0, 0)):
        super(MenuOptions, self).__init__(screen, pos)

    def create_buttons(self):
        screen = self.screen.get_rect().size
        self.buttons.append(MyButton(self.screen, option1_b, (screen[0] * 0.2, screen[1] / 2 - 70), 3, "option1"))
        self.buttons.append(MyButton(self.screen, option2_b, (screen[0] * 0.2, screen[1] / 2), 3, "option2"))
        self.buttons.append(MyButton(self.screen, option3_b, (screen[0] * 0.2, screen[1] / 2 + 70), 3, "option3"))
