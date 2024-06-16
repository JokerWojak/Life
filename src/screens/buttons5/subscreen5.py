from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SubScreen5(Screen):
    def __init__(self, **kwargs):
        super(SubScreen5, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Adding a label at the top
        layout.add_widget(Label(text="SubScreen 5", font_size='24sp'))

        # Adding 5 vertical buttons
        for i in range(1, 6):
            button = Button(text=f"Button {i}", font_size='20sp', size_hint=(1, None), height=50)
            layout.add_widget(button)

        # Adding the return button at the bottom
        return_button = Button(text="Return", font_size='20sp', size_hint=(1, None), height=50)
        return_button.bind(on_release=self.go_back)
        layout.add_widget(return_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'game'  # Navigate back to the GameScreen
