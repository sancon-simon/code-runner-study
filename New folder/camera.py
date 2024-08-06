from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import sys
import io

class CodeEditor(BoxLayout):
    def __init__(self, **kwargs):
        super(CodeEditor, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create a TextInput for the code area
        self.code_input = TextInput(
            size_hint=(1, 0.8),
            font_size=14,
            text='# Write your Python code here\n',
            multiline=True
        )

        # Create a ScrollView to make the TextInput scrollable
        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.scroll_view.add_widget(self.code_input)

        # Create a Button to run the code
        self.run_button = Button(
            text='Run Code',
            size_hint=(1, 0.1)
        )
        self.run_button.bind(on_press=self.run_code)

        # Create a Label to display the output
        self.output_label = Label(
            text='Output will be shown here',
            size_hint=(1, 0.1),
            halign='left',
            valign='top'
        )
        self.output_label.bind(size=self.output_label.setter('text_size'))

        # Add widgets to the layout
        self.add_widget(self.scroll_view)
        self.add_widget(self.run_button)
        self.add_widget(self.output_label)

    def run_code(self, instance):
        code = self.code_input.text
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        try:
            exec(code, {})
        except Exception as e:
            print(e)
        sys.stdout = old_stdout
        self.output_label.text = redirected_output.getvalue()

class CodeEditorApp(App):
    def build(self):
        return CodeEditor()

if __name__ == '__main__':
    CodeEditorApp().run()
