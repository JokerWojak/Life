from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.welcome import WelcomeScreen
from screens.game import GameScreen
from screens.buttons1.subscreen1 import SubScreen1
from screens.buttons2.subscreen2 import SubScreen2
from screens.buttons3.subscreen3 import SubScreen3
from screens.buttons4.subscreen4 import SubScreen4
from screens.buttons5.subscreen5 import SubScreen5
from persons.person import Person
from save_game import save_game

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(SubScreen1(name='subscreen1'))
        sm.add_widget(SubScreen2(name='subscreen2'))
        sm.add_widget(SubScreen3(name='subscreen3'))
        sm.add_widget(SubScreen4(name='subscreen4'))
        sm.add_widget(SubScreen5(name='subscreen5'))
        return sm

    def on_stop(self):
        # Save the game state when the application is closed
        main_character = Person()
        save_game(main_character.create_full_name(), main_character.age, None)  # Assuming bar_graph is not used on exit

if __name__ == '__main__':
    MyApp().run()
