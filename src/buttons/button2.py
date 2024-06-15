from kivy.uix.button import Button

class Button2(Button):
    def __init__(self, **kwargs):
        super(Button2, self).__init__(**kwargs)
        self.text = "Button 2"
        self.font_size = '20sp'
        self.bind(on_release=self.button_pressed)

    def button_pressed(self, instance):
        # Add logic specific to Button 1 behavior
        print("Button 2 pressed")
        # You can add more functionality specific to Button 1 here
