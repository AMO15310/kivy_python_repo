import kivy
from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        image = Image(source='/path/to/your/image.jpg',
                size_hint = (1,.5),
                pos_hint={'center_x':.5,'center_y':.5})
        return image
if __name__=="__main__":
    app = MainApp()
    app.run()
