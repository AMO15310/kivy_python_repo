import kivy
from kivy.app import App
from kivy.uix.button import Button 

class MainApp(App):
    def build(self):
        x= Button(text='Hello wrld',
                size_hint = (.5,.5),
                pos_hint = {'center_x':.5,'center_y':.5})
        return x

if __name__ == '__main__':
    app = MainApp()
    app.run()
