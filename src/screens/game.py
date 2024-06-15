import os
import json
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.app import App
from screens.widgets.bargraph import BarGraphWidget  # Ensure this import is correct

# Import your custom buttons
from buttons.button1 import Button1
from buttons.button2 import Button2
from buttons.button3 import Button3
from buttons.button4 import Button4
from buttons.button5 import Button5

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_output = TextInput(readonly=True, size_hint=(1, 0.4))
        layout.add_widget(self.text_output)

        button_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)

        # Create instances of each button and add them to the button layout
        btn1 = Button1()
        btn2 = Button2()
        btn3 = Button3()
        btn4 = Button4()
        btn5 = Button5()

        button_layout.add_widget(btn1)
        button_layout.add_widget(btn2)
        button_layout.add_widget(btn3)
        button_layout.add_widget(btn4)
        button_layout.add_widget(btn5)

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

    def save_game(self):
        # Save the current character data
        first_name, last_name = self.character_label.text.split(': ')[1].split()
        current_age = int(self.age_label.text.split(': ')[1])
        traits = self.bar_graph.get_characteristics()

        save_data = {
            'first_name': first_name,
            'last_name': last_name,
            'age': current_age,
            'traits': traits
        }

        filename = os.path.join(os.getcwd(), 'run', 'main_character.json')  # Save to 'run' folder
        try:
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=4)
            print(f"Saved game data to {filename}")
        except Exception as e:
            print(f"Error saving game data: {e}")

    def surrender_pressed(self, *args):
        App.get_running_app().stop()  # Exit the Kivy application