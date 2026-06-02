from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os

class CalculatorApp(App):
    def build(self):
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # ডিসপ্লে স্ক্রিন
        self.solution = TextInput(
            background_color="black", foreground_color="white",
            font_size=55, halign="right", multiline=False, readonly=True
        )
        main_layout.add_widget(self.solution)
        
        # ক্যালকুলেটরের বাটন লেআউট
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label, font_size=30,
                    background_color=[0.2, 0.2, 0.2, 1] if label not in self.operators else [0.9, 0.5, 0, 1]
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            
        # সমান (=) বাটন
        equals_button = Button(text="=", font_size=30, background_color=[0, 0.6, 0.2, 1])
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # এখানে ব্যাকএন্ডে আপনার C++ লজিক বা পাইথন ইভালুয়েশন কাজ করবে
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                self.solution.text = "Error"

if name == "main":
    CalculatorApp().run()