import os
import json
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.app import App
from screens.widgets.bargraph import BarGraphWidget  # Ensure this import is correct

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_output = TextInput(readonly=True, size_hint=(1, 0.4))
        layout.add_widget(self.text_output)

        button_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)
        for i in range(1, 6):
            btn = Button(text=f"Button {i}", font_size='20sp')
            btn.bind(on_release=self.button_pressed)
            button_layout.add_widget(btn)
        layout.add_widget(button_layout)

        info_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)
        self.character_label = Label(text="Name: ", font_size='20sp', size_hint=(0.6, 1))
        self.age_label = Label(text="Age: ", font_size='20sp', size_hint=(0.4, 1))
        info_layout.add_widget(self.character_label)
        info_layout.add_widget(self.age_label)
        layout.add_widget(info_layout)

        self.bar_graph = BarGraphWidget(size_hint=(1, 0.3))
        layout.add_widget(self.bar_graph)

        self.add_widget(layout)

    def on_enter(self):
        self.load_game_data()  # Load or refresh game data whenever the screen is entered

    def button_pressed(self, instance):
        self.text_output.text += f"\nButton {instance.text} pressed"

    def load_game_data(self):
        filename = os.path.join(os.getcwd(), 'run', 'main_character.json')
        try:
            with open(filename, 'r') as f:
                game_state = json.load(f)
                if 'first_name' in game_state and 'last_name' in game_state:
                    self.character_label.text = f"Name: {game_state['first_name']} {game_state['last_name']}"
                else:
                    self.text_output.text += f"\nError: Missing 'first_name' or 'last_name' in {filename}"
                if 'age' in game_state:
                    self.age_label.text = f"Age: {game_state['age']}"
                else:
                    self.age_label.text = "Age: Unknown"
                if 'traits' in game_state:
                    self.bar_graph.update_characteristics(game_state['traits'])
                else:
                    self.text_output.text += f"\nError: Missing 'traits' in {filename}"
                self.text_output.text += f"\nGame data loaded from {filename}"
        except FileNotFoundError:
            self.text_output.text += f"\nNo saved game data found at {filename}"
        except json.JSONDecodeError as je:
            self.text_output.text += f"\nError decoding JSON from {filename}: {str(je)}"

    def surrender_pressed(self, *args):
        App.get_running_app().stop()  # Exit the Kivy application
