import json
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.widget import Widget
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


Window.size = (320, 600)

with open('dict_translation_lesson.json') as type:
    dict_translation_lesson = json.load(type)

with open('tests.json') as options:
    option = json.load(options)


class Questions(Widget):
    def checkout(self, answer):
        print(answer)


class MainWindow(Screen):
    main_window = ObjectProperty(None)

    def auth(self):
        if (self.user.text and self.lastname.text and self.type.text):
            if (self.type.text[0].isdigit() and self.type.text[-1].isalpha()):
                return True
            else:
                self.ids.type.error = True
                self.ids.type.hint_text = "Класс ""пример: 5а"
        else:
            return True


class SecondWindow(Screen):
    second_screen = ObjectProperty(None)
    option = ObjectProperty(None)
    lesson = ObjectProperty(None)
    question = ObjectProperty(None)
    page = ObjectProperty(None)
    cnt = 1

    def menu_open_lesson(self, button):
        menu_items = [
            {
                "text": item,
                "on_release": lambda x=item: self.menu_callback_lesson(x),
            } for item in dict_translation_lesson
        ]

        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            position="auto"
        )
        self.menu.open()

    def menu_callback_lesson(self, text_item):
        self.ids.lesson.text = text_item
        self.menu.dismiss()

    def menu_open(self, button):

        if self.ids.lesson.text != "Предмет":
            items = option["lessons"][dict_translation_lesson.get(self.ids.lesson.text)]["options"]
        else:
            items = ["Выберите предмет"]
            
        menu_items = [
            {
                "text": item,
                "on_release": lambda x=item: self.menu_callback(x),
            } for item in items
        ]

        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            position="auto"
        )
        self.menu.open()


    def menu_callback(self, text_item, page=None, ques=None):

        # self.ids.user_profile.add_widget(Questions())

        if text_item == "Выберите предмет":
            return True

        self.ids.option.text = text_item

        dict_lesson = dict_translation_lesson.get(self.ids.lesson.text)

        watch_questions = option["lessons"][dict_lesson]["options"][text_item]["questions"]

        count_question = len(option["lessons"][dict_lesson]["options"][text_item]["questions"])

        if ques == True and count_question > self.cnt:
            self.cnt += page
            self.ids.page.text = f"{str(self.cnt)} из {count_question}"
        elif ques == False and self.cnt > 1:
            print(self.cnt)
            self.cnt += page
            self.ids.page.text = f"{str(self.cnt)} из {count_question}"
        elif ques == None and page == None:
            self.cnt = 1
            self.ids.page.text = f"{str(self.cnt)} из {count_question}"

        print(self.ids)
        
        self.ids.question.text = watch_questions[str(self.cnt)]['question']

        for i, value in enumerate(watch_questions[str(self.cnt)]['answers'], start=1):
            if i == 1:
                self.ids.answer_1.text = value
            elif i == 2:
                self.ids.answer_2.text = value

        self.menu.dismiss()


    def checkout(self, answer):
        print(answer)


class WindowManager(ScreenManager):
    manager = ObjectProperty(None)


class VPRApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_pallete = "Teal"
        self.theme_cls_accent_hue = "400"
        self.root = Builder.load_file("main.kv")


if __name__ == "__main__":
    VPRApp().run()
