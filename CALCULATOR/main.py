from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.opreator = ["/", "*", "+", "- "]
        self.icon = "calculator.png"
        self.last_was_opreator = None
        self.last_button = None

        main_layout = BoxLayout(orientaion="veritcal")
        self.solution = TextInput(background_color="black", foreground_color="white",
                                  multiline=False, halign="right", font_size=55)

        main_layout.add_widget(self.solution)
        button = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"]
        ]

        for row in button:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=h_layout, font_size=30, background_color="grey", pos_hint
                    ={"center_x ": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(text="=", font_size=30, backgorund_color ="grey",
                              pos_hint={"center_x": 0.5, "center_y": 0.5})

        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "c":
            self.solution.text == ""
        else:
            if current and (self.last_was_opreator and button_text in self.opreator):
                return
            elif current == "" and button_text in self.opreator:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

            self.last_button = button_text
            self.last_was_opreator = self.last_button

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution









if __name__ == "__main__":
    app = MainApp()
    app.run()





