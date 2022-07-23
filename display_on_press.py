import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        x = Button(text = 'Click me!!',
                size_hint=(.5,.6),
                pos_hint={'center_x':.5,'center_y':.5})
        x.bind(on_press=self.on_press_button)
        return x
    def on_press_button(self,instance):
        self.y =  print("You clicked me!!")
        return self.y

if __name__ == '__main__':
    app = MainApp()
    app.run()
