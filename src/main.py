from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.welcome import WelcomeScreen
from screens.game import GameScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    MyApp().run()
