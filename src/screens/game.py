import os
import json
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.app import App
from screens.widgets import BarGraphWidget

class GameScreen(Screen):
    character_label = ObjectProperty(None)
    bar_graph = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.character_label = Label(text="Character Name", font_size='20sp', size_hint=(1, None), height=50)
        layout.add_widget(self.character_label)

        self.bar_graph = BarGraphWidget(size_hint=(1, 0.6))
        layout.add_widget(self.bar_graph)

        button_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)

        surrender_button = Button(text="Surrender", font_size='20sp')
        surrender_button.bind(on_release=self.surrender_pressed)
        button_layout.add_widget(surrender_button)

        layout.add_widget(button_layout)
        self.add_widget(layout)

        self.load_game_data()  # Load initial data when GameScreen is initialized

    def update_characteristics(self, new_values):
        self.bar_graph.update_characteristics(new_values)

    def load_game_data(self):
        filename = os.path.join(os.getcwd(), 'run', 'main_character.json')
        try:
            with open(filename, 'r') as f:
                game_state = json.load(f)
                if 'first_name' in game_state and 'last_name' in game_state:
                    self.character_label.text = f"{game_state['first_name']} {game_state['last_name']}"
                else:
                    print(f"Error: Missing 'first_name' or 'last_name' in {filename}")
                if 'traits' in game_state:
                    self.bar_graph.update_characteristics(game_state['traits'])
                else:
                    print(f"Error: Missing 'traits' in {filename}")
                print(f"Game data loaded from {filename}")
        except FileNotFoundError:
            print(f"No saved game data found at {filename}")
        except json.JSONDecodeError as je:
            print(f"Error decoding JSON from {filename}: {str(je)}")

    def surrender_pressed(self, *args):
        App.get_running_app().stop()  # Exit the Kivy application
