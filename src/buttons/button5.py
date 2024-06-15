from kivy.uix.button import Button

class Button5(Button):
    def __init__(self, **kwargs):
        super(Button5, self).__init__(**kwargs)
        self.text = "Button 5"
        self.font_size = '20sp'
        self.bind(on_release=self.button_pressed)

    def button_pressed(self, instance):
        # Add logic specific to Button 1 behavior
        print("Button 5 pressed")
        # You can add more functionality specific to Button 1 here
