from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SubScreen2(Screen):
    def __init__(self, **kwargs):
        super(SubScreen2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="SubScreen 2", font_size='24sp'))
        self.add_widget(layout)
