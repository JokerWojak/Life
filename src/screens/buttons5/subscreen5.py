from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SubScreen5(Screen):
    def __init__(self, **kwargs):
        super(SubScreen5, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="SubScreen 5", font_size='24sp'))
        self.add_widget(layout)
