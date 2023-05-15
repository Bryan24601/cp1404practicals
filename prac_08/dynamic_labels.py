from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabels(App):
    names = ['Bob', 'Juliet', 'Chicken', 'Carlos']

    def build(self):
        self.title = "Dynamic Labels"
        root = Builder.load_file('dynamic_labels.kv')
        labels_box = root.ids.labels
        for current_name in self.names:
            label = Label(text=current_name)
            labels_box.add_widget(label)
        return root


DynamicLabels().run()
