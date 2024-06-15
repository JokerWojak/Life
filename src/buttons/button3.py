from kivy.uix.button import Button
from kivy.app import App


class Button3(Button):
    def __init__(self, **kwargs):
        super(Button3, self).__init__(**kwargs)
        self.text = "Age Up"
        self.font_size = '20sp'
        self.bind(on_release=self.on_release)

    def on_release(self, instance):
        game_screen = App.get_running_app().root.get_screen('game')
        current_age = int(game_screen.age_label.text.split(': ')[1])
        new_age = current_age + 1
        game_screen.age_label.text = f"Age: {new_age}"

        # Save the updated character data
        game_screen.save_game()

        # Update the text output
        game_screen.text_output.text += f"\nAge: {new_age}"
