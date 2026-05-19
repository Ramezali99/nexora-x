from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.08, 0.08, 0.1, 1)

class NexoraApp(App):

    def build(self):

        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        self.title_label = Label(
            text="NEXORA X",
            font_size=32,
            size_hint=(1, 0.2)
        )

        self.input_box = TextInput(
            hint_text="Ask Nexora AI...",
            multiline=False,
            size_hint=(1, 0.15)
        )

        self.send_button = Button(
            text="Send",
            size_hint=(1, 0.15)
        )

        self.send_button.bind(on_press=self.process_text)

        self.output_label = Label(
            text="Response will appear here",
            font_size=18
        )

        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.send_button)
        self.layout.add_widget(self.output_label)

        return self.layout

    def process_text(self, instance):

        user_text = self.input_box.text.strip()

        if user_text == "":
            self.output_label.text = "Please enter a message."
            return

        self.output_label.text = f"Nexora AI: {user_text}"

if __name__ == "__main__":
    NexoraApp().run()