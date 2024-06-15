import random
import os
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from screens.widgets.bargraph import BarGraphWidget  # Ensure this import is correct
from persons.character import Person
from save_game import save_game
from load_game import load_game

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.character_label = Label(text='', font_size='20sp', size_hint=(1, None), height=50)
        layout.add_widget(self.character_label)

        self.age_label = Label(text='Age: 0', font_size='20sp', size_hint=(1, None), height=50)
        layout.add_widget(self.age_label)

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
        # Save the current character data
        save_game(self.character_label, self.age_label, self.bar_graph)

        # Print statement for debugging
        print("Accept button pressed")

        # Update the graph with the current data
        self.update_graph_with_current_data()

        # Switch to the 'game' screen
        self.manager.current = 'game'

    def next_pressed(self, *args):
        new_character = Person()
        self.character_label.text = new_character.create_full_name()

        # Update age in UI
        self.age_label.text = f"Age: {new_character.age}"

        new_values = {
            'Health': random.randint(0, 100),
            'Smarts': random.randint(0, 100),
            'Looks': random.randint(0, 100),
            'Happiness': random.randint(0, 100)
        }
        self.bar_graph.update_characteristics(new_values)

        save_game(self.character_label, self.age_label, self.bar_graph)  # Save the newly generated character data

    def update_graph_with_current_data(self):
        current_traits = self.bar_graph.get_characteristics()
        self.bar_graph.update_characteristics(current_traits)

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
        load_game(self.character_label, self.age_label, self.bar_graph)

    def find_saved_games(self):
        saved_games = [filename for filename in os.listdir(os.getcwd()) if filename.endswith(".json")]
        return saved_games
