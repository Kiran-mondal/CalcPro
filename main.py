import numpy as np
import sympy as sp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class AdvancedQuantumCalculator(App):
    def build(self):
        self.operators = ["+", "-", "*", "/"]
        
        # Main layout of the application
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Display Screen for input and output
        self.display = TextInput(
            background_color="black", 
            foreground_color="white",
            font_size=35, 
            halign="right", 
            multiline=True, 
            readonly=True
        )
        main_layout.add_widget(self.display)
        
        # Grid layout for calculator buttons
        button_grid = GridLayout(cols=4, spacing=10)
        
        # Array of button labels including standard, matrix, and quantum functions
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["Matrix Det", "EigenVal", "Schrodinger", "="]
        ]
        
        # Generating and styling buttons dynamically
        for row in buttons:
            for label in row:
                if label in ["=", "Matrix Det", "EigenVal", "Schrodinger"]:
                    btn_color = [0.9, 0.5, 0, 1] # Orange color for advanced functions
                elif label == "C":
                    btn_color = [0.7, 0, 0, 1] # Red color for clear button
                else:
                    btn_color = [0.2, 0.2, 0.2, 1] # Dark grey for numbers and basic operators
                    
                btn = Button(text=label, font_size=18, background_color=btn_color)
                btn.bind(on_press=self.on_button_click)
                button_grid.add_widget(btn)
                
        main_layout.add_widget(button_grid)
        return main_layout

    def on_button_click(self, instance):
        text = instance.text
        current_text = self.display.text
        
        if text == "C":
            self.display.text = ""
        elif text == "=":
            self.calculate_standard()
        elif text == "Matrix Det":
            self.calculate_matrix_determinant()
        elif text == "EigenVal":
            self.calculate_eigenvalues()
        elif text == "Schrodinger":
            self.solve_schrodinger_equation()
        else:
            self.display.text = current_text + text

    # 1. Standard Mathematics Calculation
    def calculate_standard(self):
        try:
            result = str(eval(self.display.text))
            self.display.text = result
        except Exception:
            self.display.text = "Error in Expression"

    # 2. Advanced Matrix Determinant Solver (High Speed via NumPy)
    def calculate_matrix_determinant(self):
        try:
            # Expected Input Format on screen: [[1,2],[3,4]]
            matrix_data = eval(self.display.text)
            matrix_array = np.array(matrix_data)
            determinant = np.linalg.det(matrix_array)
            self.display.text = f"Matrix Det:\n{str(determinant)}"
        except Exception:
            self.display.text = "Input Error!\nUse Format: [[1,2],[3,4]]"

    # 3. Quantum Mechanics: Matrix Eigenvalues Solver
    def calculate_eigenvalues(self):
        try:
            # Expected Input Format on screen: [[1,0],[0,-1]]
            matrix_data = eval(self.display.text)
            matrix_array = np.array(matrix_data)
            eigenvalues = np.linalg.eigvals(matrix_array)
            self.display.text = f"Eigenvalues:\n{str(eigenvalues)}"
        except Exception:
            self.display.text = "Input Error!\nUse Format: [[1,0],[0,-1]]"