from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar

class BarGraphWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(BarGraphWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.traits = {}
        self.labels = {}

        # Initialize characteristics with default values and labels
        for trait in ['Health', 'Smarts', 'Looks', 'Happiness']:
            self.add_trait(trait, 0)

    def add_trait(self, trait_name, initial_value):
        # Create a horizontal layout for each trait
        bar_layout = BoxLayout(orientation='horizontal')

        # Trait label
        trait_label = Label(text=trait_name, size_hint=(0.2, 1))
        bar_layout.add_widget(trait_label)

        # Progress bar
        bar = ProgressBar(max=100, value=initial_value, size_hint=(0.7, 1), height=30)
        bar_layout.add_widget(bar)

        # Value label
        value_label = Label(text=str(initial_value), size_hint=(0.1, 1))
        bar_layout.add_widget(value_label)

        # Store references to bar and value label
        self.traits[trait_name] = bar
        self.labels[trait_name] = value_label

        # Add the bar_layout to the BarGraphWidget
        self.add_widget(bar_layout)

    def update_trait(self, trait_name, value):
        if trait_name in self.traits:
            self.traits[trait_name].value = value
            self.labels[trait_name].text = str(value)

    def update_characteristics(self, new_values):
        for trait, value in new_values.items():
            self.update_trait(trait, value)

    def get_characteristics(self):
        characteristics = {}
        for trait, bar in self.traits.items():
            characteristics[trait] = int(bar.value)
        return characteristics
