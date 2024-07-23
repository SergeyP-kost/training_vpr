from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty


Window.size = (320, 600)


class MainWindow(Screen):

    def auth(self):
        if (self.user.text and self.lastname.text and self.type.text):
            if (self.type.text[0].isdigit() and self.type.text[-1].isalpha()):
                with open('data.txt', 'w', encoding='utf-8') as f:
                    f.write(f'{self.user.text},{self.lastname.text},{self.type.text}')
                return True
            else:
                self.ids.type.error = True
                self.type.helper_text = "Ошибка. Введите номер и букву класса"
        else:
            return True #заглушка для проверки (удалить)

                
class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class VPRApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_pallete = "Teal"
        self.theme_cls_accent_hue = "400"

        self.root = Builder.load_file("main.kv")
    

if __name__ == "__main__":
    VPRApp().run()
