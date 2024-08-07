from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from instructions import * 

Window.clearcolor = (.26, .99, 1.21, 1)
lbl_color = (.29, .32, .4, .1)
btn_color = (.14, .32, .4, 1)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst_lbl = Label(text=txt_instruction, color=lbl_color, bold=True)
        name_lbl = Label(text="Введіть ім'я", color=lbl_color, bold=True, font_size=30)
        self.name_input = TextInput(text="Микола", multiline=False)
        age_lbl = Label(text="Введіть вік", color=lbl_color, bold=True, font_size=30)
        self.age_input = TextInput(text="7", multiline=False)

        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=15,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={"center_x": .5}
        )
        line1 = BoxLayout(size_hint=(.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(.8, None), height="30sp")

        line1.add_widget(name_lbl)
        line1.add_widget(self.name_input)

        line2.add_widget(age_lbl)
        line2.add_widget(self.age_input)

        main_line = BoxLayout(orientation="vertical", padding=30, spacing=20)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)







class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class ResultScreen(Screen): 
    pass


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.real_add_widget(MainScreen(name='main'))
        sm.real_add_widget(SecondScreen(name='second'))
        sm.real_add_widget(ThirdScreen(name='thsrd'))
        sm.real_add_widget(FourthScreen(name='fourth'))
        sm.real_add_widget(ResultScreen(name='result'))
        return sm
    

app = HeartCheck()
app.run()
