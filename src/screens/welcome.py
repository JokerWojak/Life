import random
import json
import os
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from screens.widgets.bargraph import BarGraphWidget  # Ensure this import is correct
from persons.character import Person


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.character_label = Label(text='', font_size='20sp', size_hint=(1, None), height=50)
        layout.add_widget(self.character_label)

        self.bar_graph = BarGraphWidget(size_hint=(1, 0.6))
        layout.add_widget(self.bar_graph)

        button_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)
        self.accept_button = Button(text="Accept", font_size='20sp')
        self.accept_button.bind(on_release=self.accept_pressed)
        button_layout.add_widget(self.accept_button)

        self.next_button = Button(text="Next", font_size='20sp')
        self.next_button.bind(on_release=self.next_pressed)
        button_layout.add_widget(self.next_button)

        load_button = Button(text="Load Game", font_size='20sp')
        load_button.bind(on_release=self.load_game_options)
        button_layout.add_widget(load_button)

        layout.add_widget(button_layout)
        self.add_widget(layout)

        self.load_game()  # Load initial character data on screen creation

    def accept_pressed(self, *args):
        self.save_game()  # Save the current character data
        print("Accept button pressed")
        game_screen = self.manager.get_screen('game')
        game_screen.load_game_data()  # Ensure game screen loads the latest data
        self.manager.current = 'game'

    def next_pressed(self, *args):
        new_character = Person()
        self.character_label.text = new_character.create_full_name()

        new_values = {
            'Health': random.randint(0, 100),
            'Smarts': random.randint(0, 100),
            'Looks': random.randint(0, 100),
            'Happiness': random.randint(0, 100)
        }
        self.bar_graph.update_characteristics(new_values)

        self.save_game(new_character, new_values)  # Save the newly generated character data

    def save_game(self, new_character=None, new_values=None):
        if new_character and new_values:
            save_data = {
                'first_name': new_character.first_name,
                'last_name': new_character.last_name,
                'traits': new_values
            }
        else:
            first_name, last_name = self.character_label.text.split()
            save_data = {
                'first_name': first_name,
                'last_name': last_name,
                'traits': self.bar_graph.get_characteristics()
            }

        filename = os.path.join(os.getcwd(), 'run', 'main_character.json')  # Save to 'run' folder
        try:
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=4)
            print(f"Saved game data to {filename}")
        except Exception as e:
            print(f"Error saving game data: {e}")

    def load_game_options(self, *args):
        saved_games = self.find_saved_games()
        content = BoxLayout(orientation='vertical', spacing=10)
        popup = Popup(title='Load Game', content=content, size_hint=(None, None), size=(400, 400))

        for game_name in saved_games:
            btn = Button(text=game_name, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.load_game(game_name))
            content.add_widget(btn)

        popup.open()

    def load_game(self, game_name=None):
        filename = os.path.join(os.getcwd(), 'run', 'main_character.json')  # Load from 'run' folder

        try:
            with open(filename, 'r') as save_file:
                game_state = json.load(save_file)
                first_name = game_state.get('first_name', 'Unknown')
                last_name = game_state.get('last_name', 'Unknown')
                self.character_label.text = f"{first_name} {last_name}"
                self.bar_graph.update_characteristics(
                    game_state.get('traits', {}))  # Default to empty dict if 'traits' is missing
                print(f"Loaded game data from {filename}")
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
        except json.JSONDecodeError as je:
            print(f"Error decoding JSON from {filename}: {str(je)}")

    def find_saved_games(self):
        # Function to find all JSON files in the 'run' directory
        saved_games = [filename for filename in os.listdir('run') if filename.endswith(".json")]
        return saved_games
