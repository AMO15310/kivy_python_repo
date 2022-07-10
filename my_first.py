#import all the necessary kivy modules
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

#make a class name it Main
class MainApp(App):
    def build(self):
        #define the button properties
        button = Button(text='Press Me',
                 size_hint=(.5,.5),
                 pos_hint={'center_x':.5,'center_y':.5})
                 #Bind the button functionality
        button.bind(on_press=self.press_p)
        return button
    def press_p(self,instance):
        print("You Clicked the button")
#run the application
if __name__=='__main__':
    MainApp().run()
