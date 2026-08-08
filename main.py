from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Calculator(App):

    def build(self):
        main = BoxLayout(
            orientation="vertical",
            padding=8,
            spacing=5
        )

        self.entry = TextInput(
            text="",
            readonly=True,
            halign="right",
            font_size=32,
            size_hint_y=0.2
        )
        main.add_widget(self.entry)

        buttons = GridLayout(cols=4, spacing=5)

        keys = [
            "7", "8", "9", "÷",
            "4", "5", "6", "×",
            "1", "2", "3", "-",
            "C", "0", ".", "+"
        ]

        for key in keys:
            button = Button(text=key, font_size=24)

            if key == "C":
                button.bind(on_press=self.clear)
            else:
                button.bind(on_press=self.press)

            buttons.add_widget(button)

        main.add_widget(buttons)

        equal = Button(
            text="=",
            font_size=28,
            size_hint_y=0.15
        )
        equal.bind(on_press=self.equal)
        main.add_widget(equal)

        return main

    def press(self, instance):
        value = instance.text

        if value == "×":
            value = "*"
        elif value == "÷":
            value = "/"

        self.entry.text += value

    def clear(self, instance):
        self.entry.text = ""

    def equal(self, instance):
        try:
            result = eval(self.entry.text)
            self.entry.text = str(result)
        except:
            self.entry.text = "Error"


Calculator().run()
