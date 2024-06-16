import os
import json
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from screens.widgets.bargraph import BarGraphWidget
from load_game import load_game
from save_game import save_game

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_output = TextInput(readonly=True, size_hint=(1, 0.4))
        layout.add_widget(self.text_output)

        button_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)

        button1 = Button(text="Button 1", font_size='20sp')
        button1.bind(on_release=lambda x: self.change_screen('subscreen1'))
        button_layout.add_widget(button1)

        button2 = Button(text="Button 2", font_size='20sp')
        button2.bind(on_release=lambda x: self.change_screen('subscreen2'))
        button_layout.add_widget(button2)

        button3 = Button(text="Button 3", font_size='20sp')
        button3.bind(on_release=lambda x: self.change_screen('subscreen3'))
        button_layout.add_widget(button3)

        button4 = Button(text="Button 4", font_size='20sp')
        button4.bind(on_release=lambda x: self.change_screen('subscreen4'))
        button_layout.add_widget(button4)

        button5 = Button(text="Button 5", font_size='20sp')
        button5.bind(on_release=lambda x: self.change_screen('subscreen5'))
        button_layout.add_widget(button5)

        layout.add_widget(button_layout)

        info_layout = BoxLayout(size_hint=(1, None), height=50, orientation='horizontal', spacing=10)
        self.character_label = Label(text="Name: ", font_size='20sp', size_hint=(0.6, 1))
        self.age_label = Label(text="Age: 0", font_size='20sp', size_hint=(0.4, 1))  # Initial age is 0
        info_layout.add_widget(self.character_label)
        info_layout.add_widget(self.age_label)
        layout.add_widget(info_layout)

        self.bar_graph = BarGraphWidget(size_hint=(1, 0.3))
        layout.add_widget(self.bar_graph)

        self.add_widget(layout)

    def change_screen(self, screen_name):
        app = App.get_running_app()
        app.root.current = screen_name

    def on_enter(self):
        load_game(self.character_label, self.age_label, self.bar_graph)  # Load game data when screen is entered
