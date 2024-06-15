from kivy.uix.button import Button
from kivy.app import App

class Button3(Button):
    def __init__(self, **kwargs):
        super(Button3, self).__init__(**kwargs)
        self.text = "Age Up"
        self.font_size = '20sp'
        self.size_hint = (1, None)
        self.height = 50

    def on_release(self):
        app = App.get_running_app()
        game_screen = app.root.get_screen('game')
        current_age = int(game_screen.age_label.text.split(': ')[1])
        new_age = current_age + 1
        game_screen.age_label.text = f"Age: {new_age}"
        game_screen.text_output.text += f"\nCurrent Age: {new_age}"
        game_screen.save_game()  # Save the current state
