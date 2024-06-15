from kivy.uix.button import Button

class Button1(Button):
    def __init__(self, **kwargs):
        super(Button1, self).__init__(**kwargs)
        self.text = "Button 1"
        self.font_size = '20sp'
        self.bind(on_release=self.button_pressed)

    def button_pressed(self, instance):
        # Add logic specific to Button 1 behavior
        print("Button 1 pressed")
        # You can add more functionality specific to Button 1 here
